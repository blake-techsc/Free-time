from tkinter import *
root = Tk()

root.title("GUI Test")
root.geometry('400x400')

lbl = Label(root, text = "What's up?")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

def clicked():

    res = "You wrote " + txt.get()
    lbl.configure(text = res)

btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
btn.grid(column=1, row=1)

root.mainloop()