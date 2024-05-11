# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'An Overview and Simple Guide to Environmental DNA Protocols and Workflows'
copyright = '2024, the authors'
author = 'Orianne Tournayre, Haolun (Allen) Tian, Stafford "Rotehrá:kwas" Maracle, and Stephen C. Lougheed'

release = '2.1'
version = '2.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

#    - Assign numbers to figures
numfig = True
numfig_secnum_depth = 0

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for PDF output
latex_engine = 'xelatex'
latex_elements = {
    'maketitle': r"""
    \author{Orianne Tournayre, Haolun (Allen) Tian, \and Stafford "Rotehrá:kwas" Maracle, \and and Stephen C. Lougheed}
    \sphinxmaketitle
    """,
    # https://tex.stackexchange.com/questions/55404/how-to-remove-chapter-name-with-fncychap-package
    'fncychap': r"""
    \usepackage[Sonny]{fncychap}
    \renewcommand\FmN[1]{}
    """,
}
