import time
import ENIGMA as en
from tkinter import *
from tkinter import messagebox, Label, scrolledtext


def encode(code,text):
    if(len(str(code.get()))!=5):
        code.configure(bg='red')
        messagebox.showinfo('AV Industries', "ENTER A 5-DIGIT STARTING CODE")
    else:
        try:
            #code.configure(bg='light blue')
            codes = int(code.get())
            #for i in range(10000, codes + 1):
            txt = en.encode(text.get("1.0", "end-1c"), codes)
            text.delete(1.0,'end')
            text.insert(1.0,txt)
                #time.sleep(0.0001)
        except ValueError:
            code.configure(bg='red')
            messagebox.showinfo('AV Industries',"ENTER A NUMERIC STARTING CODE")

#__MAIN__

w = Tk()
w.geometry('1360x768')
w.resizable(False, False)
titlex = ' ' * 150 + 'VILAKSHAN\'S ENIGMA MACHINE - Encryption Software by AV Industries'
w.title(titlex)

i_code_l = Label(w, font=('Arial 22 bold'), text='Starting Code(5-digit number):')
i_code_e = Entry(w, font='Arial 35 bold', width = 5)
t_l = Label(w, font=('Arial 22 bold'), text='Your Text :')
t_e = scrolledtext.ScrolledText(w, font=('Monotype Corsiva', 22),height=12,width = 85)
btn = Button(w, text='Encrypt or Decrypt', width = 90, font=('Monotype Corsiva',18),bg='blue',fg='white',command=lambda:[encode(i_code_e,t_e)])

i_code_l.pack()
i_code_e.pack()
t_l.pack()
t_e.pack()
btn.pack()

'''
i_code_l.place(x=50, y=10)
i_code_e.place(x=280, y=10)
t_l.place(x=50, y=110)
t_e.place(x=280, y=110)
btn.place(x=900, y=620)'''
w.mainloop()
