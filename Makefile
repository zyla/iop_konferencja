all: iop.html

iop.md: gienierator.py
	python3 gienierator.py > .iop.md && mv .iop.md iop.md

iop.html: iop.md
	pandoc --toc -s iop.md > iop.html
