import sys,os
#add set suffix / prefix
#add incrementing suffix / prefix

delimiter = command = command_pos = text = write = ''
pdfs = [pdf for pdf in os.listdir() if pdf.endswith('.pdf') or pdf.endswith('.PDF')]
pdfs = sorted(pdfs)
if pdfs:
    print('pdfs located')
    response = input('do you want to see pdfs found? y/n... ')
    if response == 'y':
        print(pdfs)
else:
    print('nothing found')
    exit = input('... ')
    sys.exit()

print('-----------------\n')
print('delimiter: "_", ".", "-", " " etc.')
delimiter = input('please input a delimiter... ')
print('-----------------\n')

print('commands: "static", "increment"')
command = input('please input command... ')
print('-----------------\n')

print('pos: "prefix", "suffix"')
command_pos = input('please input a position... ')
print('-----------------\n')

text = input('please submit text... ') 
print(f'text will be separated from filename with "{delimiter}".')
print('-----------------\n')

if command == "increment":
    print('write: "append", "overwrite"')
    write = input('please submit write type... ')

if command == 'static':
       
    if command_pos == 'prefix':
        for pdf in pdfs:
            os.rename(pdf,f'{text}{delimiter}{pdf}')

    else: #suffix

        for pdf in pdfs:
            os.rename(pdf,f'{pdf[:-4]}{delimiter}{text}.pdf')

else: #increment
    if command_pos == 'prefix':
        for pos,pdf in enumerate(pdfs):
            if write == "overwrite":
                os.rename(pdf,f'{text}{delimiter}{pos+1}{delimiter}.pdf')

            else: #append
                os.rename(pdf,f'{text}{delimiter}{pos+1}{delimiter}{pdf}')

    else: #suffix
        for pos,pdf in enumerate(pdfs):
            if write == "overwrite":
                try:
                    os.rename(pdf,f'{text}{delimiter}{pos+1}.pdf')   
                except FileExistsError:
                    print('naming clash, please rectify first.')
                    exit_ = input()
                    sys.exit()
                    
            else: #append
                os.rename(pdf,f'{pdf[:-4]}{delimiter}{text}{delimiter}{pos+1}.pdf')