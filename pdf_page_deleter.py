from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os,sys

pdfs = [f for f in os.listdir() if f.endswith('.PDF') or f.endswith('.pdf')]

if len(pdfs) > 1:
    print('too many files found')
    sys.exit()
elif not pdfs:
    print('no files found')
    sys.exit()

pdf = pdfs[0] # select input pdf
reader = PdfFileReader(pdf)

print('either give a number, or separate numbers with a "," comma')
delete = input('what pages are to be deleted?...')

delete = delete.split(',')
ignore_pages = []
for items in delete:
    ignore_pages.append(int(items))

writer = PdfFileWriter()

for pagenum in range (reader.getNumPages()):
    if pagenum+1 in ignore_pages:
        continue

    page = reader.getPage(pagenum)
    writer.addPage(page)

with open(f'editied_pdf.pdf','wb') as out:
    writer.write(out)
