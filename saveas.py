from tkinter import filedialog

def SaveFileAs(text):
    file = filedialog.asksaveasfile(mode='a+', defaultextension='.txt')
    file.write(text)
    file.flush()
    file.close()
    
