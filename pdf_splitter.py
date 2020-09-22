# pdf splitter using PyPDF2
#test line

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os,sys

positive_response = ['y','yes','ye','yeah','yep','sure','yeah','positive',"true"]
negative_response = ['n','no','nope','negative','ne','nep','nah','',None,'false'] # completely redundant but nice to have

pdfs = [f for f in os.listdir() if f.endswith('.PDF') or f.endswith('.pdf')]

if len(pdfs) > 1:
    print('too many files found')
    sys.exit()
elif not pdfs:
    print('no files found')
    sys.exit()

while True:
    double_scan = input('are the pdfs double scanned? y/n ... ')
    if double_scan in positive_response or double_scan in negative_response:
        break
    else:
        print('false input detected')

purge = input('do you want to delete output PDF used? y/n ... ')

pdf = pdfs[0] # select input pdf
reader = PdfFileReader(pdf)

i=0
for pagenum in range (reader.getNumPages()):
    if double_scan in positive_response and not pagenum %2 ==0:
        print('page skipped')
        continue

    page = reader.getPage(pagenum)

    writer = PdfFileWriter()
    writer.addPage(page)
    if double_scan in positive_response:
        page2 = reader.getPage(pagenum+1)
        writer.addPage(page2)

    i += 1
    with open(f'page_{i}.pdf','wb') as out:
        writer.write(out)

if purge in positive_response:
    os.remove(pdf)