#!/bin/bash
find . -name "*.png" -exec convert -units PixelsPerInch {} -density 130 {}-scaled.png \;