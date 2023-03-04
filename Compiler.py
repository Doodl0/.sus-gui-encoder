from tkinter import *
import tkinter.ttk as ttk
from random import randint

char = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\n']
code = ""

window = Tk()
window.title("C Sus Sus GUI Compiler")
window.columnconfigure([0,1,2,3],weight=10)
window.rowconfigure([0,1],weight=10)

window.call("source", "azure.tcl")
window.call("set_theme", "light")

switch = IntVar()

def switchClicked():
    if switch.get() :
        window.call("set_theme", "dark")
    else :
        window.call("set_theme", "light")

title=ttk.Entry(textvariable=StringVar())
title.grid(row=0,column=1,sticky="we")
text=Text()
text.grid(row=1,column=1)
scrollbarY=ttk.Scrollbar(orient='vertical',command=text.yview)
scrollbarY.grid(row=1,column=0,sticky="ns")
text['yscrollcommand'] = scrollbarY.set
darkmodeswitch = ttk.Checkbutton(text="Dark Mode", style="Switch.TCheckbutton",variable = switch,onvalue = 1, offvalue = 0, command=switchClicked)
darkmodeswitch.grid(row=1,column=3,sticky="se")


def saveAsSus():
    filename=title.get()
    code=text.get('1.0','end')
    with open(f"sus\{filename}.sus", "w") as compiled:
        for c in code:
            if c in char:
                compiled.write("s"*char.index(c))
                compiled.write("\n")


def saveAsPy():
    filename=title.get()
    filecontent=text.get('1.0','end')

    with open(f"py\{filename}.py","w") as file:
        file.write(filecontent)

def loadAsPy():
    filename=title.get()

    with open(f"py\{filename}.py", "r") as file:
        code = file.read()
    text.delete("1.0",END)
    text.insert("1.0",code)

def loadAsSus():
    filename=title.get()

    with open(f"sus\{filename}.sus", "r") as file:
        code = file.read()
    text.delete("1.0",END)
    text.insert("1.0",code)

def loadSusAsPy():
    filename=title.get()

    with open(f"sus\{filename}.sus", "r") as file:
        code = file.read()
    index = 0
    
    text.delete("1.0",END)
    for c in code:
        if c == "s":
            index += 1
        elif c == "\n":
            if index > len(char)-1:
                index = len(char)-1
            text.insert("end",char[index])
            index = 0



savepy=ttk.Button(text="Save as .py",command=saveAsPy,style="Accent.TButton")
savepy.grid(row=1,column=3,sticky="ne")
savesus=ttk.Button(text="Save as .sus",command=saveAsSus,style="Accent.TButton")
savesus.grid(row=1,column=3,sticky="e")

loadpy=ttk.Button(text="Load .py",command=loadAsPy,style="Accent.TButton")
loadpy.grid(row=1,column=2,sticky="se")
loadsus=ttk.Button(text="Load .sus",command=loadAsSus,style="Accent.TButton")
loadsus.grid(row=1,column=2,sticky="e")
loadsuspy=ttk.Button(text="Load .sus as .py",command=loadSusAsPy,style="Accent.TButton")
loadsuspy.grid(row=1,column=2,sticky="ne")

window.mainloop()
