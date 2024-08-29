# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'An Overview and Simple Guide to Environmental DNA Protocols and Workflows'
copyright = '2024, the authors'
author = 'Orianne Tournayre, Haolun (Allen) Tian, Stafford "Rotehrá:kwas" Maracle, David R. Lougheed, and Stephen C. Lougheed'
# To edit the authors on the cover page of the PDF, edit latex_elements["maketitle"] below

release = '2.2'
version = '2.2.0'

# -- General configuration

root_doc = "index"
html_static_path = ["_static"]

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
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
html_css_files = [
    'css/custom.css'
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for PDF output
latex_engine = 'xelatex'
latex_documents = [
    (root_doc, "eDNA_manual.tex", project, author, "manual")
]
latex_elements = {
    # 'extrapackages': r"\usepackage{titling}",
    'maketitle': r"""
    \author{Orianne Tournayre$^{1,2}$, Haolun (Allen) Tian$^1$, \and Stafford "Rotehrá:kwas" Maracle$^1$, 
    David Lougheed$^3$, \and and Stephen C. Lougheed$^1$}
    \date{
    1. Department of Biology, Queen’s University, Kingston, Ontario, Canada \\
    2. Current address. Department of Biology, York University, Toronto, Ontario, Canada \\
    3. Canadian Centre for Computational Genomics, McGill University, Montreal, Quebec, Canada \\~\\
    \centering
    \normalfont 
    \textit{Originally prepared for the Queen’s University Biological Station environmental DNA workshop} \\~\\
    \includegraphics[width=2in]{QUBS}
    \\~\\~\\
    DOI: \href{https://doi.org/10.5281/zenodo.13421371}{10.5281/zenodo.13421371}
    }
    \sphinxmaketitle
    """,
    # https://tex.stackexchange.com/questions/55404/how-to-remove-chapter-name-with-fncychap-package
    'fncychap': r"""
    \usepackage[Sonny]{fncychap}
    \renewcommand\FmN[1]{}
    """,
    # For tcolorbox see https://tex.stackexchange.com/questions/371007/how-to-make-a-box-in-the-sense-of-see-box-1
    'preamble': r"""
    \usepackage{pdflscape}
    \usepackage{tcolorbox}
    \newtcolorbox[auto counter]{mybox}[1][]{float,title={Box~\thetcbcounter},#1}
    """,
}
latex_additional_files = ["images/QUBS.png"]
