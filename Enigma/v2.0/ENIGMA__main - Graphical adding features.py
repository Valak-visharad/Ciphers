import ENIGMA as en
from tkinter import *
from tkinter import messagebox, Label, scrolledtext
from PIL import Image, ImageTk

def encode(code, text):
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
        except ValueError:
            code.configure(bg='red')
            messagebox.showinfo('AV Industries',"ENTER A NUMERIC STARTING CODE")

def spec_page():
    l_key = Label (w, text = 'Pass key : ', font = ('arial', 20)).place (x = 390, y = 300)
    e_key = Entry (w, border = 5, font = 'arial 20', show = 'x', bg = 'light yellow', fg = 'red', width = 20).place(x = 550, y = 300)
    btn = Button (w, image = nxt_image, command = lambda : [check_key(l_key, e_key, btn)]).place(x = 880, y = 295)
    # print('inside spec')

#__MAIN__

w = Tk()
w.geometry('1360x768')
w.resizable(False, False)
#titlex = ' ' * 150 + 'Encryption Software by AV Industries'
w.title('enigma')
w.wm_iconbitmap('enigma.ico')

i_code_l = Label(w, font=('Arial 22 bold'), text='Starting Code(5-digit number):')
i_code_e = Entry(w, font='Arial 35 bold', width = 5)
t_l = Label(w, font=('Arial 22 bold'), text='Your Text :')
t_e = scrolledtext.ScrolledText(w, font=('Monotype Corsiva', 22),height=12,width = 85)
btn = Button(w, text='Encrypt or Decrypt', width = 90, font=('Monotype Corsiva',18),bg='blue',fg='white',command=lambda:[encode(i_code_e,t_e)])

spec_btn = Button(w, text = 'ENIGMA', width = 90, height = 2, command = lambda : [spec_page(), i_code_l.pack_forget(), i_code_e.pack_forget(), t_l.pack_forget(), t_e.pack_forget(), btn.pack_forget(), spec_btn.pack_forget()])

spec_btn.pack()
i_code_l.pack()
i_code_e.pack()
t_l.pack()
t_e.pack()
btn.pack()

nxt_image = ImageTk.PhotoImage(Image.open('next.jpg'))

'''
i_code_l.place(x=50, y=10)
i_code_e.place(x=280, y=10)
t_l.place(x=50, y=110)
t_e.place(x=280, y=110)
btn.place(x=900, y=620)'''
w.mainloop()
