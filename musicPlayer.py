from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
import os

filetoplay = ''

def selfile():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Track File", filetypes=(("Music File", "*.mp3"), ("All files", "*.*")))
    txt.set(os.path.basename(fln))
    filetoplay = fln


root = Tk()

txt = StringVar()
txt.set("Track: No track selected")

root.title("Simple Music Player v1")

wrapper = LabelFrame(root, text="Music Player")
wrapper.pack(fill="both", expand="yes")

lbl = Label(wrapper, textvariable=txt)
lbl.pack

btn1 = Button(wrapper, text="Select Track", command=selfile)
btn1.pack(side=tk.LEFT, padx=10)

root.geometry("400x150")
root.resizable(True,True)
root.mainloop()