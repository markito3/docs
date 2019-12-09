all: mywork.pdf

mywork.aux: mywork.tex
	latex mywork

mywork.blg: spires.bib mywork.aux
	bibtex mywork

mywork.pdf: mywork.blg mywork.tex
	pdflatex mywork
	pdflatex mywork
