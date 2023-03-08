from tkinter import *
from tkinter.filedialog import *
import tkinter.ttk as ttk
from random import randint

char = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\n']
code = ""

window = Tk()
window.title("C Sus Sus GUI Compiler")
window.columnconfigure([0],weight=0)
window.columnconfigure([1],weight=1)
window.rowconfigure([0],weight=1)

window.call("source", "azure.tcl")
window.call("set_theme", "light")

switch = IntVar()
def switchClicked():
    if switch.get() :
        window.call("set_theme", "dark")
    else :
        window.call("set_theme", "light")


text=Text()
text.grid(row=0,column=1,sticky="nsew")
scrollbarY=ttk.Scrollbar(orient='vertical',command=text.yview)
scrollbarY.grid(row=0,column=0,sticky="nsew")
text['yscrollcommand'] = scrollbarY.set

def saveAsSus():
    
    code=text.get('1.0','end')

    compiled = asksaveasfile(mode='w', defaultextension=".sus", filetypes=[('C Sus Sus Files', '*.sus')])
    if compiled is None:
        return
    
    for c in code:
        if c in char:
            compiled.write("s"*char.index(c))
            compiled.write("\n")


def saveAsPy():
    
    filecontent=text.get('1.0','end')

    compiled = asksaveasfile(mode='w', defaultextension=".py", filetypes=[('Python Files', '*.py')])
    if compiled is None: 
        return

    compiled.write(filecontent)

def loadAsPy():
    file = askopenfile(mode='r', defaultextension=".py", filetypes=[('Python Files', '*.py')])
    if file is None: 
        return

    code = file.read()
    text.delete("1.0",END)
    text.insert("1.0",code)

def loadAsSus():
    file = askopenfile(mode='r', defaultextension=".sus", filetypes=[('C Sus Sus Files', '*.sus')])
    if file is None: 
        return

    code = file.read()
    text.delete("1.0",END)
    text.insert("1.0",code)

def loadSusAsPy():
    file = askopenfile(mode='r', defaultextension=".sus", filetypes=[('C Sus Sus Files', '*.sus')])
    if file is None: 
        return

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

def newfile():
    text.delete("1.0",END)

mainmenu = Menu()
filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "New File", command = newfile)
filemenu.add_separator()
filemenu.add_command(label = "Save as .sus", command = saveAsSus)
filemenu.add_command(label = "Save as .py", command =  saveAsPy)
filemenu.add_separator()
filemenu.add_command(label = "Load .sus as .py", command = loadSusAsPy)
filemenu.add_command(label = "Load .sus", command = loadAsSus)
filemenu.add_command(label = "Load .py", command = loadAsPy)
mainmenu.add_cascade(label="File", menu=filemenu)
optionsmenu = Menu(mainmenu, tearoff = 0)
optionsmenu.add_checkbutton(label = "Dark Mode", variable = switch,onvalue = 1, offvalue = 0, command=switchClicked)
mainmenu.add_cascade(label="Options", menu=optionsmenu)

window.config(menu = mainmenu)

window.mainloop()
