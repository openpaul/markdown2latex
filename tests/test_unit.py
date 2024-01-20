from mdx_latex import (
    LaTeXExtension,
    escape_latex_entities,
    inline_html_latex,
    makeExtension,
    unescape_html_entities,
    unescape_latex_entities,
)
import markdown


def test_inline_html_latex():
    input_text = "&ldquo;Sample text&rdquo; &lsquo;Another text&rsquo; &laquo;Yet another text&raquo; ..."
    expected_output = "\\enquote{Sample text} \\enquote{Another text} \\enquote{Yet another text} \dots"

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


def test_basic():
    text = "Simple test"
    output = markdown.markdown(text, extensions=[LaTeXExtension()])

    expected_output = "Simple test"

    assert output == expected_output


def test_header():
    text = "## Simple test"
    output = markdown.markdown(text, extensions=[LaTeXExtension()])

    expected_output = "\\section{Simple test}"

    assert output == expected_output


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


def test_math_basic():
    # simple inline math
    simple_md = "This is $1+2$ inline math."
    expected = "This is \\(1+2\\) inline math."
    output = markdown.markdown(simple_md, extensions=[LaTeXExtension()])
    assert output == expected

    # simple block math
    simple_md = "This is $$1+2$$ inline math."
    expected = "This is \\[1+2\\] inline math."
    output = markdown.markdown(simple_md, extensions=[LaTeXExtension()])
    assert output == expected

    # a simple dollar sign
    simple_md = "I only have $13 left."
    expected = "I only have \\$13 left."
    output = markdown.markdown(simple_md, extensions=[LaTeXExtension()])
    assert output == expected

    # All together now
    markdown_text = "Some mathematics inline, $$X$$, $Y$, a $100 million, a %tage and then a formula:"
    expected_output = "Some mathematics inline, \\[X\\], \\(Y\\), a \\$100 million, a \\%tage and then a formula:"

    output = markdown.markdown(markdown_text, extensions=[LaTeXExtension()])

    assert output == expected_output

def test_formular():

    md  = "$$ \\sum_{i}^{\\infty} x^{n} + y^{n} = \\alpha +  \\beta * z^{n} $$"

    expected_output = "\\[ \\sum_{i}^{\\infty} x^{n} + y^{n} = \\alpha +  \\beta \cdot z^{n} \\]"

    output = markdown.markdown(md, extensions=[LaTeXExtension()])
    assert output == expected_output
