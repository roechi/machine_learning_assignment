#!/bin/bash
pandoc --toc --toc-depth=2 -s -N -V fontsize=12pt -V geometry:margin=1in  --include-in-header titlesec.tex -o bericht_holland_remus.pdf bericht_holland_remus.md
