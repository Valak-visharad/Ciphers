import ENIGMA as en
while True:
    try:
        cod=input("STARTING CODE:")
        while(len(cod)!=5):
            print("\n\t\t\t\t\t:::::ERROR OCCURED:::::\n\t\t\tSOL: ENTER A 5-DIGIT CODE")
            cod=input("STARTING CODE:")
        code=int(cod)
        txt=list(input("\nNOTE:\nIf you are pasting it from a source, paste it by not leaving space!\nYour text:"))
        print(en.encode(txt,code))
    except: print("\n\t\t\t\t\t:::::ERROR OCCURED:::::\n\t\t\tSOL: ENTER NUMERIC CODE")
