#!/bin/bash
#pandoc --toc --toc-depth=2 -s -N -V fontsize=12pt -V geometry:margin=1in  --include-in-header titlesec.tex -o bericht_holland_remus.pdf bericht_holland_remus.md

pandoc --filter pandoc-citeproc --toc -s -N -V fontsize=12pt -V geometry:margin=1in bericht_holland_remus.md --biblio bericht.bib --include-in-header titlesec.tex --csl springer-lecture-notes-in-computer-science_modified.csl -o bericht_holland_remus.pdf
