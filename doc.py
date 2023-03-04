"""Extension to python-markdown to support LaTeX (rather than html) output.

Authored by Rufus Pollock: <http://www.rufuspollock.org/>
Reworked by Julian Wulfheide (ju.wulfheide@gmail.com) and
Pedro Gaudencio (pmgaudencio@gmail.com)

Usage:
======

1. Command Line. A script entitled markdown2latex.py is automatically
installed. For details of usage see help::

    $ markdown2latex.py -h

2. As a python-markdown extension::

    >>> import markdown
    >>> md = markdown.Markdown(None, extensions=['latex'])
    >>> # text is input string ...
    >>> latex_out = md.convert(text)

3. Directly as a module (slight inversion of std markdown extension setup)::

    >>> import markdown
    >>> import mdx_latex
    >>> md = markdown.Markdown()
    >>> latex_mdx = mdx_latex.LaTeXExtension()
    >>> latex_mdx.extendMarkdown(md, markdown.__dict__)
    >>> out = md.convert(text)

History
=======

Version: 1.0 (November 15, 2006)

  * First working version (compatible with markdown 1.5)
  * Includes support for tables

Version: 1.1 (January 17, 2007)

  * Support for verbatim and images

Version: 1.2 (June 2008)

  * Refactor as an extension.
  * Make into a proper python/setuptools package.
  * Tested with markdown 1.7 but should work with 1.6 and (possibly) 1.5
    (though pre/post processor stuff not as worked out there)

Version 1.3: (July 2008)
  * Improvements to image output (width)

Version 1.3.1: (August 2009)
  * Tiny bugfix to remove duplicate keyword argument and set zip_safe=False
  * Add [width=\textwidth] by default for included images

Version 2.0: (June 2011)
  * PEP8 cleanup
  * Major rework since this was broken by new Python-Markdown releases

Version 2.1: (August 2013)
  * Add handler for non locally referenced images, hyperlinks and horizontal rules
  * Update math delimiters
"""

__version__ = '2.1'
