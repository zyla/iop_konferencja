all: iop.html

pdf: iop.pdf

iop.md: gienierator.py
	python3 gienierator.py > .iop.md && mv .iop.md iop.md

iop.html: iop.md
	pandoc --toc -s iop.md > iop.html

iop.pdf: iop.md
	pandoc -s iop.md -o iop.pdf
