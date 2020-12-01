# pdf splitter using PyPDF2
#test line

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os,sys,math

positive_response = ['y','yes','ye','yeah','yep','sure','yeah','positive',"true"]
negative_response = ['n','no','nope','negative','ne','nep','nah','',None,'false'] # completely redundant but nice to have

pdfs = [f for f in os.listdir() if f.endswith('.PDF') or f.endswith('.pdf')]

if len(pdfs) > 1:
    print('too many files found')
    exit_ = input()
    sys.exit()
elif not pdfs:
    print('no files found')
    exit_ = input()
    sys.exit()

if 'index.txt' in os.listdir():
    os.remove('index.txt')
    print('purged old index')
    
while True:
    double_scan = input('are the pdfs double scanned? y/n ... ')
    if double_scan in positive_response or double_scan in negative_response:
        break
    else:
        print('false input detected')

purge = input('do you want to delete output PDF used? y/n ... ')

pdf = pdfs[0] # select input pdf
reader = PdfFileReader(pdf)

index = input('do you want to save an index card? y/n ... ')

for pagenum in range(reader.getNumPages()):
    if double_scan in positive_response and not pagenum %2 ==0:
        continue

    page = reader.getPage(pagenum)

    writer = PdfFileWriter()
    writer.addPage(page)

    try:
        if double_scan in positive_response:
            page2 = reader.getPage(pagenum+1)
            writer.addPage(page2)

    except:
        pass

    with open(f'page_{pagenum+1}.pdf','wb') as out:
        writer.write(out)

if index in positive_response:
    with open('index.txt','w') as write_index:
        if double_scan in positive_response:
            index_ = [str(i) for i in range(1,math.floor(reader.getNumPages()/2)+1)]
        else:
            index_  = [str(i) for i in range(1,reader.getNumPages()+1)]
        write_index.write('\n'.join(index_))


if purge in positive_response:
    os.remove(pdf)