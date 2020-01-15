#NONSTOP =  -interaction=nonstopmode

all: mywork.pdf

mywork.aux: mywork.tex
	latex mywork

mywork.bbl : spires.bib mywork.aux
	bibtex mywork

mywork.pdf: mywork.bbl mywork.tex
	cp -pv mywork.aux mywork.aux.tmp
	pdflatex $(NONSTOP) mywork
	pdflatex $(NONSTOP) mywork
	if diff mywork.aux.tmp mywork.aux ; then mv -v mywork.aux.tmp mywork.aux ; fi

clean:
	$(RM) -v *.aux mywork.pdf *.log *.bbl *.blg *.dvi
