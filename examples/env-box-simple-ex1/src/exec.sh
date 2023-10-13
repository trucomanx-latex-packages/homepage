#!/bin/bash


pdflatex -shell-escape example
pdflatex -shell-escape example
pdflatex -shell-escape example

pdftoppm -r 300 example.pdf example -png

convert -trim example-1.png example-1.png




./clean.sh example
