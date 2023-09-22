def morse(line, morse_dict = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '.-.-'}):
    '''
    i)  Single space b/w two letters.
    ii) Double space b/w two words.
    iii) you can copy paste too.
    Converts morse into English and vice versa automatically.
    '''
    line = line.lower()
    morsers = list(morse_dict.values())
    alphas = list(morse_dict.keys())
    words = line.split()
    out = ''
    for x in words:
        if x[0] == "." or x[0] == "-":
            try:    out += alphas[morsers.index(x)]
            except: out += x
        else:
            for dx in x:
                try:    out += morse_dict[dx]
                except: out += x
                else:   out += ' '
        out += ' ' 
    return out
    