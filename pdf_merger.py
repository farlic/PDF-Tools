# pdf merger using PyPDF2
from PyPDF2 import PdfFileMerger
import os,sys

positive_response = ['y','yes','ye','yeah','yep','sure','yeah','positive',"true"]
negative_response = ['n','no','nope','negative','ne','nep','nah','',None,'false'] # completely redundant but nice to have

pdfs = [f for f in os.listdir() if f.endswith('.pdf') or f.endswith('.PDF')]
lines = ''

if 'output.pdf' in pdfs:
    os.remove('output.pdf')
    print('purging old output')
    pdfs.remove('output.pdf')

if not pdfs:
    print('no pdfs found, exiting...')
    sys.exit()

index = input('do you want to stort by index file? y/n ... ')

if index in positive_response:
    try:
        with open('index.txt','r') as f:
            lines = [line.strip() for line in f.readlines()]
            
    except FileNotFoundError:
        print('no index found')
        exit_ = input('... ')
        sys.exit()

else:
    try:
        pdfs.sort(key=lambda x: int(x.split('.')[0][5:]))
    except ValueError:
        print('bad filenames, please format as page_{num}')
        exit_ = input()
        sys.exit()

if lines:
    for pos,line in enumerate(lines):
        if line.isnumeric():
            lines[pos] = f'page_{line}.pdf'
        else:
            lines[pos] = f'{line}.pdf'
    pdfs = lines
            


show_pdfs = input('do you want to see PDFs detected? y/n ... ')
if show_pdfs in positive_response:
    print(pdfs)

purge = input('do you want to delete files used? y/n ... ')

merger = PdfFileMerger(strict=False)
for pdf in pdfs:
    merger.append(pdf)

merger.write('output.pdf')
merger.close() # clears memory stream

if purge in positive_response: # if the purge is before closing the memory access will give permission denied
    for pdf in pdfs:
        os.remove(pdf)