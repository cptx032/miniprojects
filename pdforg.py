#!/usr/bin/python
# coding: utf-8

# Autor: Willie Lawrence
# Este script foi criado originalmente em Mon 14 Oct 2013 08:41:20 PM UTC

def getArg(arg):
	try:
		return sys.argv[sys.argv.index(arg) + 1]
	except:
		pass

def arredondar(arg1, arg2):
	resultDivision = arg1 / float(arg2)
	# verificando existencia de numero decimal
	dec = int( str(resultDivision).split(".")[-1] )
	if dec > 0:
		resultDivision += 1
	return int(resultDivision)

def getNumFolhas(pdf):
	return arredondar(pdf.getNumPages(), 4)

from pyPdf import PdfFileWriter, PdfFileReader
import sys

def showDoc():
	print """-F : The entry file
-B : The block size
-C : The output pdf file name"""
	sys.exit(0)

if "--help" in sys.argv:
	showDoc()

FILE_NAME = getArg("-F")
ENTRY_PDF = PdfFileReader(file(FILE_NAME, "rb"))
BLANK_PAGE = PdfFileReader(file(r"resources/blank_page.pdf", "rb")).getPage(0)
BLOCK_SIZE = None
try:
	BLOCK_SIZE = int(getArg("-B")) or getNumFolhas(ENTRY_PDF)
except:
	BLOCK_SIZE = getNumFolhas(ENTRY_PDF)

assert type(BLOCK_SIZE) == int, "The block must be a integer"
OUT_FILE_NAME = getArg("-C") or "pdf_organizer_output.pdf"

# _____________LOGIC____________

class Folha(object):
	def __init__(self):
		self.page0 = None
		self.page1 = None
		self.page2 = None
		self.page3 = None
	
	def __repr__(self):
		return "P1: %s\nP2: %s\nP3: %s\nP4: %s\n" % (self.page0, self.page1,
			self.page2, self.page3)

BLOCKS = []
HOW_MANY_BLOCKS = arredondar( getNumFolhas(ENTRY_PDF), BLOCK_SIZE )
# BLOCK_SIZE: quantas folhas tem um bloco // uma folha tem 4 páginas
# HOW_MAY_BLOCKS: quantos blocos existem no projeto atual

# ______________PREENCHENDO OS BLOCOS COM FOLHAS VAZIAS________________
for i in range(HOW_MANY_BLOCKS):
	BLOCKS.append( [Folha() for i in range(BLOCK_SIZE)] )


# ____________________POSTANDO O NÚMERO DAS PÁGINAS_____________________
N_PAGINAS = range(ENTRY_PDF.getNumPages())
ACTUAL_PAGE = 0

for block in BLOCKS:
	for page in block:
		try:
			page.page0 = N_PAGINAS[ACTUAL_PAGE]
			ACTUAL_PAGE += 1
			page.page1 = N_PAGINAS[ACTUAL_PAGE]
			ACTUAL_PAGE += 1
		except:
			print "Actual page: " + str(ACTUAL_PAGE)
			break
	# ____________________PERCORRENDO A LISTA NO SENTIDO INVERSO______________________
	for i in range(len(block)):
		p = block[len(block)-1 - i]
		try:
			p.page2 = N_PAGINAS[ACTUAL_PAGE]
			ACTUAL_PAGE += 1
			p.page3 = N_PAGINAS[ACTUAL_PAGE]
			ACTUAL_PAGE += 1
		except:
			break
"""	
for block in BLOCKS:
	for i in range(len(block)):
		p = block[len(block)-1 - i]
		try:
			p.page2 = N_PAGINAS[ACTUAL_PAGE]
			ACTUAL_PAGE += 1
			p.page3 = N_PAGINAS[ACTUAL_PAGE]
			ACTUAL_PAGE += 1
		except:
			break"""
# ______________________REMOVENDO PAGINAS EM BRANCO________________________
for block in BLOCKS:
	for page in block:
		if page.page0 == None and page.page1 == None and page.page2 == None and page.page3 == None:
			block.remove(page)

# _______________ORGANIZANDO AS PÁGINAS__________________

output = PdfFileWriter()

for block in BLOCKS:
	for page in block:
		try:
			output.addPage( ENTRY_PDF.getPage( page.page1 ) )
		except:
			output.addPage(BLANK_PAGE)
		try:
			output.addPage( ENTRY_PDF.getPage( page.page2 ) )
		except:
			output.addPage(BLANK_PAGE)
		try:
			output.addPage( ENTRY_PDF.getPage( page.page3 ) )
		except:
			output.addPage(BLANK_PAGE)
		try:
			output.addPage( ENTRY_PDF.getPage( page.page0 ) )
		except:
			output.addPage(BLANK_PAGE)

outStream = file(OUT_FILE_NAME, "wb")
output.write(outStream)
outStream.close()
