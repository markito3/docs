all: mywork.pdf

mywork.aux: mywork.tex
	latex mywork

mywork.bbl : spires.bib mywork.aux
	bibtex mywork

mywork.pdf: mywork.bbl mywork.tex
	pdflatex mywork
	pdflatex mywork

clean:
	$(RM) -v *.aux mywork.pdf *.log *.bbl *.blg *.dvi
