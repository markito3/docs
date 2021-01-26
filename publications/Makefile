ifdef NONSTOP
  PDFLATEX_OPTIONS = -interaction=nonstopmode
endif

all: mywork.pdf

mywork.aux_for_bib: mywork.tex
	latex mywork
	mv -v mywork.aux $@

mywork.bbl : spires.bib mywork.aux_for_bib
	cp -p mywork.aux_for_bib mywork.aux
	bibtex mywork

mywork.pdf: mywork.bbl mywork.tex
	pdflatex $(PDFLATEX_OPTIONS) mywork
	pdflatex $(PDFLATEX_OPTIONS) mywork

clean:
	$(RM) -v *.aux mywork.pdf *.log *.bbl *.blg *.dvi *.tmp
