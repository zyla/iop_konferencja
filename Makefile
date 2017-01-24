all: iop.html

pdf: iop.pdf

iop.md: gienierator.py
	python3 gienierator.py > .iop.md && mv .iop.md iop.md

iop.html: iop.md diagram_klas.png
	pandoc --toc -s iop.md > iop.html

iop.pdf: iop.md diagram_klas.png
	pandoc -s iop.md -o iop.pdf

diagram_klas.png: iop.dia
	dia --export=diagram_klas.png iop.dia
