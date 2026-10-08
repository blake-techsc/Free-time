# THIS IS BLAKE'S CODE

from tkinter import *
from tkinter import messagebox
import pyqrcode

ws = Tk()
ws.title("QR Code Gen")
ws.config(bg="#d2edff")

def genQR():
    if len(user_input.get())!=0:
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning("Warning!","All fields are required :p")
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of" + user_input.get())

lbl = Label(
    ws,
    text="Enter URL",
    bg="#d2edff"
)
lbl.pack()

user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
)
entry.pack(padx=10)

button = Button(
    ws,
    text = "Generate",
    width = 7,
    command = genQR
    )
button.pack(pady=10)

img_lbl = Label(
    ws,
    bg = "#d2edff")
img_lbl.pack()

output = Label(
    ws,
    text = "",
    bg = "#d2edff"
)

output.pack()

ws.mainloop()