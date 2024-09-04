# An Overview and Guide to Environmental DNA Protocols and Workflows

[![Documentation Status](https://readthedocs.org/projects/edna-manual/badge/?version=stable)](https://edna-manual.readthedocs.io/en/stable/?badge=stable)
[![10.5281/zenodo.13421371](https://zenodo.org/badge/DOI/10.5281/zenodo.13421371.svg)](https://doi.org/10.5281/zenodo.13421371)

[Orianne Tournayre](https://oriannetournayre.wixsite.com/website) (1, 2), 
[Haolun (Allen) Tian](https://allensgallery.ca/) (1), 
Stafford “Rotehrá:kwas” Maracle (1),
[David R. Lougheed](https://dlougheed.com/) (3),
and [Stephen C. Lougheed](https://sclougheed.ca/) (1).

1. Department of Biology, Queen’s University, Kingston, Ontario, Canada
2. Current address. Department of Biology, York University, Toronto, Ontario, Canada
3. Canadian Centre for Computational Genomics, McGill University, Montreal, Quebec, Canada


*Originally prepared for the Queen’s University Biological Station environmental
DNA workshop*

CC-BY-4.0 Creative Commons License 2022-2024

*This has been a ‘living document’ that we have continued to edit & update each year and will continue to do so.*

**How to cite this document:** Tournayre, O. Tian, H., Maracle, S., R., & Lougheed, S. C. (2024). An overview and guide 
to environmental DNA protocols and workflows. Version 2.2. Queen’s University, Kingston, Ontario, Canada. 
DOI: [10.5281/zenodo.13421371](https://doi.org/10.5281/zenodo.13421371)

> **Note:** The DOI provided here links to all versions of the source code for this document. To access a specific 
> version's DOI, [see here](https://zenodo.org/search?q=parent.id%3A13421371&f=allversions%3Atrue&l=list&p=1&s=10&sort=version)
> or click "View all [n] versions" on the Zenodo page for a specific document version.


## Project Structure

The manual is created using the Sphinx tool, and section text is written in the 
[reStructuredText (RST)](https://docutils.sourceforge.io/docs/user/rst/quickref.html) format (also see the 
[Sphinx tutorial](https://sphinx-tutorial.readthedocs.io/), which has some additional information on using RST).

The project is roughly structured as follows:

* Section files are stored in the [./src/sections](./src/sections) folder. 
* Images are stored in the [./src/images](./src/images) and should be high-resolution and, preferably, PNGs.
* Tables are stored either as images or as CSVs in [./src/tables](./src/tables) folder, or alternatively are defined 
  in-line in the section RST files.
