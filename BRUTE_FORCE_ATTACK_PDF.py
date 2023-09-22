import PyPDF2 as pd

filename=input("Path to the file")

file=open(filename,'rb')
pdfreader=pd.PdfFileReader(file)

tried=0

if not pdfReader.isEncrypted:
    print('The file is not encrypted!\n\t\tACCESS GAINED')

else:
    wordListFile=open('dictionary.txt','r')
    body=wordListFile.read().lower()
    words=body.split('\n')

    for i in range(len(words)):
        word=word[i]
        print('Tryin decription by: {}'.format(word))
        result=pdfReader.decrypt(word)
        if result==1:
            print('ACCESS GRANTEED!\nTHE PASSWORD IS: '+word)
            break
        elif result==0:
            tried+=1
            print("Paswwords Tried: "+str(tried))
            continue
