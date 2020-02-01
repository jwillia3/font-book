#!/usr/bin/env python3
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *

titlefont = 'serif 36'
exampletext = 'The quick brown fox jumped over the lazy dog'

# Select which fonts are listed in the navigation panel
def setlist(onlyfixed):
    fontlist.delete(0, END)
    for family in fixedfamilies if onlyfixed else families:
        fontlist.insert(END, family)

# Display font specimen
def displayfont(family):
    for child in display.winfo_children():
        child.destroy()

    Label(display, text = family, font = titlefont).pack(pady = 18)

    for size in range(10, 38, 2):
        Label(display,
            text = f'{size}pt {exampletext}',
            font = f'"{family}" {size}').pack(fill = 'x')

def fixedtoggled():
    setlist(bool(fixedvar.get()))
    fontlist.focus()

def selectionchanged(event):
    displayfont(fontlist.get(fontlist.curselection()[0]))

def isfixedpitched(family):
    font = Font(family = family, size = 10, weight = BOLD)
    return font.measure('M') == font.measure('i')

root = Tk()
fixedvar = IntVar(value = 1)
families = sorted(set(tkinter.font.families()))
fixedfamilies = list(filter(isfixedpitched, families))

root.title('Font Book')
style = Style()
for i in ['TFrame', 'TLabel', 'Listbox', 'TCheckbutton']:
    style.configure(i, foreground = 'black', background = 'white')

# Set up window
window = PanedWindow(root, orient = HORIZONTAL, width = 1000)
window.pack(fill = BOTH, expand = True)

# Set up the navigation panel
navigation = Frame()
Checkbutton(
    navigation,
    text = 'Only Fixed-Pitched',
    command = fixedtoggled,
    variable = fixedvar).pack(fill = 'x', pady = 10)
fontlist = Listbox(navigation, exportselection = False)
fontlist.bind('<<ListboxSelect>>', selectionchanged);
fontlist.pack(fill = BOTH, expand = True)
window.add(navigation)

# Display field
display = Frame()
display.pack()
window.add(display)

# Nice defaults
setlist(bool(fixedvar.get()))
displayfont(fontlist.get(0))
fontlist.focus()

mainloop()
