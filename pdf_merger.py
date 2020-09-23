# pdf merger using PyPDF2
from PyPDF2 import PdfFileMerger
import os,sys

positive_response = ['y','yes','ye','yeah','yep','sure','yeah','positive',"true"]
negative_response = ['n','no','nope','negative','ne','nep','nah','',None,'false'] # completely redundant but nice to have

pdfs = [f for f in os.listdir() if f.endswith('.pdf') or f.endswith('.PDF')]

if 'output.pdf' in pdfs:
    os.remove('output.pdf')
    print('purging old output')
    pdfs.remove('output.pdf')

if not pdfs:
    print('no pdfs found, exiting...')
    sys.exit()

pdfs.sort(key=lambda x: int(x.split('.')[0][5:]))

show_pdfs = input('do you want to see PDFs detected? y/n ... ')
if show_pdfs in positive_response:
    print(pdfs)

purge = input('do you want to delete PDFs used? y/n ... ')

merger = PdfFileMerger(strict=False)
for pdf in pdfs:
    merger.append(pdf)

merger.write('output.pdf')
merger.close() # clears memory stream

if purge in positive_response: # if the purge is before closing the memory access will give permission denied
    for pdf in pdfs:
        os.remove(pdf)