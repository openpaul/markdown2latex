from math import exp
import markdown
import pytest

from mdx_latex import (
    Img2Latex,
    LaTeXExtension,
    escape_latex_entities,
    inline_html_latex,
    makeExtension,
    unescape_html_entities,
    unescape_latex_entities,
)


def test_inline_html_latex():
    input_text = "&ldquo;Sample text&rdquo; &lsquo;Another text&rsquo; &laquo;Yet another text&raquo; ..."
    expected_output = "\\enquote{Sample text} \\enquote{Another text} \\enquote{Yet another text} \\dots"

    result = inline_html_latex(input_text)

    assert result == expected_output


def test_unescape_html_entities():
    input_text = "This &amp; is &lt; a &quot;test&quot; string."
    expected_output = 'This & is < a "test" string.'

    result = unescape_html_entities(input_text)

    assert result == expected_output


def test_escape_latex_entities():
    input_text = "This & is % a # test string."
    expected_output = "This \\& is \\% a \\# test string."

    result = escape_latex_entities(input_text)

    assert result == expected_output


def test_unescape_latex_entities():
    input_text = "This \\& is a test string."
    expected_output = "This & is a test string."

    result = unescape_latex_entities(input_text)

    assert result == expected_output


def test_makeExtension():
    ext = makeExtension()
    assert isinstance(ext, LaTeXExtension)


def test_items():
    markdown_text = """## A first section ##

A simple list:

  1. Item 1
  2. Item 2"""
    expected_output = """\\section{A first section}

A simple list:

\\begin{enumerate}

  \\item Item 1
  \\item Item 2
\\end{enumerate}"""
    assert (
        markdown.markdown(markdown_text, extensions=[LaTeXExtension()])
        == expected_output
    )


@pytest.mark.parametrize(
    "markdown_text,expected_output",
    [
        ("Hello World", "Hello World"),
        ("## Hello World", "\\section{Hello World}"),
        ("### Hello World", "\\subsection{Hello World}"),
        ("Hello $World$", "Hello \\(World\\)"),
        ("Hello $$World$$", "Hello \\[World\\]"),
        ("Hello $World", "Hello \\$World"),
        ("Hello **World**", "Hello \\textbf{World}"),
        (
            "$$ \\sum_{i}^{\\infty} x^{n} + y^{n} = \\alpha +  \\beta * z^{n} $$",
            "\\[ \\sum_{i}^{\\infty} x^{n} + y^{n} = \\alpha +  \\beta \\cdot z^{n} \\]",
        ),
        (
            "Some mathematics inline, $$X$$, $Y$, a $100 million, a %tage and then a formula:",
            "Some mathematics inline, \\[X\\], \\(Y\\), a \\$100 million, a \\%tage and then a formula:",
        ),
        (
            "A table now (this is *really* complicated):",
            "A table now (this is \\emph{really} complicated):",
        ),
        ("[link](https://example.com)", "\\href{https://example.com}{link}"),
    ],
)
def test_one_line(markdown_text: str, expected_output: str):
    output = markdown.markdown(markdown_text, extensions=[LaTeXExtension()])
    assert output == expected_output


@pytest.mark.parametrize(
    "markdown_text,expected_output",
    [
        ("Multiple\nLines", "Multiple\nLines"),
        (
            '![Alt caption text](link to image.webp "Title field")',
            """\\begin{figure}[H]
            \\centering
            \\includegraphics[max width=\\linewidth]{link to image.webp}
            \\caption{Alt caption text}
            \\end{figure}""",
        ),
    ],
)
def test_multi_line(markdown_text: str, expected_output: str):
    output = markdown.markdown(markdown_text, extensions=[LaTeXExtension()])
    assert output == expected_output


def test_Img2Latex():
    html_text = '<img alt="Hello" src="Dragster.jpg" />'
    expected_output = """
            \\begin{figure}[H]
            \\centering
            \\includegraphics[max width=\\linewidth]{Dragster.jpg}
            \\caption{Hello}
            \\end{figure}
            """
    converter = Img2Latex()
    output = converter.convert(html_text)
    assert output == expected_output
