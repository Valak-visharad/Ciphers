from international_MORSE_code import *
print("MORSE BY VILAKSHAN\nSome rules:\nspace between words\t\t\t\t\"<space*3>\"\nspace between letters of the same words\t\"<space>\"\ndot-   (.)\ndash-  (-)\nend othe line \t\t\t\t\"<space>\"")
while True:
    line = input('>>> ')
    print(morse(line)+"\n")

