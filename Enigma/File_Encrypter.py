import ENIGMA as en
filename=input("Enter the address of the file to be ENCRYPTED : ")
try:
    text=open(filename,"r")
    print('text : \n',text.read())
    t=text.read()
    txt=en.encode(t)
    print("txt",txt)
    text.close()
    text=open(filename,"w")
    text.write(str(txt))
    text.flush()
    text.close()
    print("Encrypted Succesfully")
except:
    print('Sorry File doesn\'t exists')
