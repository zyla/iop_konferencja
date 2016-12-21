all: iop.html

iop.md: gienierator.py
	python3 gienierator.py > iop.md

iop.html: iop.md
	pandoc -s iop.md > iop.html
