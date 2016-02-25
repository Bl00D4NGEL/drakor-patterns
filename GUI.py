import sys
import time
import pattern
from Tkinter import *
from threading import Timer

"""
This GUI is created by Dominik Peters.
You are free to use and modify it at any given time.
"""

tradeskills = ["Smithing","Cooking","Alchemy", "Crafting", "Construction", "Inscription", "Enchanting", "Jewelcrafting"]
saveList = ["gui_smithing.txt", "gui_cooking.txt", "gui_alchemy.txt", "gui_crafting.txt", "gui_construction.txt", "gui_inscription.txt", "gui_enchanting.txt", "gui_jewelcrafting.txt"] #Open Document to read from

mGui = Tk()
def ListBoxChange():
    lb_index = 0
    try:
        now = mListBox.get(mListBox.curselection())
    except:
        now = ""
        lb_index = -1
    if now == "Smithing":
        lb_index = 0
    if now == "Cooking":
        lb_index = 1
    if now == "Alchemy":
        lb_index = 2
    if now == "Crafting":
        lb_index = 3
    if now == "Construction":
        lb_index = 4
    if now == "Inscription":
        lb_index = 5
    if now == "Enchanting":
        lb_index = 6
    if now == "Jewelcrafting":
        lb_index = 7
    if lb_index > -1:
        mListBox2.delete(0, END) #clear   
        f = open(saveList[lb_index], "r")
        for line in f:
            mListBox2.insert(END, line)
    time.sleep(0.5)
    GetPatternFromLb()
    ListBoxChange()

    
def GetPatternFromLb():
    try:
        pattern = mListBox2.get(mListBox2.curselection())
        pattern = pattern.lower()             # Convert the string into lower-case just for the if-case convenience
        pattern = pattern.replace(" ", "_")   # Replace any Spaces with underscores so no unnecessary errors get thrown
        pattern = pattern[:-1]
        PrintPattern(pattern, 1, 0)
    except:
        pass
  
def mGetPattern():
    myString = mEntryPattern.get()          # Read the pattern that the user put in 
    myString = myString.lower()             # Convert the string into lower-case just for the if-case convenience
    myString = myString.replace(" ", "_")   # Replace any Spaces with underscores so no unnecessary errors get thrown  
    myInt = int(mSpinBox.get())             # Read the quantity the user put in
    
    if myInt > 0:                           # If the user (accidently) inputs a number equal or under 0 write error into label
        try:                                # Try to parse arguments into function, otherwise write error into label
            PrintPattern(myString,myInt,0)
        except AttributeError:
            mLabel2['text'] = "ERROR!!! \n The pattern you have entered is not valid!"
            mLabel2['bg'] = "Red"
            
    else:
        mLabel2['text'] = "ERROR!!! \n The number you have entered is not valid!"
        mLabel2['bg'] = "Red"

def PrintPattern(pattern_name, quan, indent):
    getattr(pattern,pattern_name)(quan, indent)
    labelText= ""
    for x in pattern.pattern_tree:
        labelText= labelText + ("\t" * x['indent'])+ "[" + x['name'] + "] x%d" % (x['quan']) + "\n"
    pattern.pattern_tree = []
    mLabel2['bg'] = "Green"
    mLabel2['text'] = labelText

    
mGui.geometry("900x900")
mGui.title("Patterns!")

mInfoPattern=Label(mGui, text="Hello there! \n Please enter your pattern you wish to know!", justify="left")
mInfoPattern.grid(row = 0, sticky = "W")

mEntryPattern = Entry(mGui, justify="left")
mEntryPattern.grid(row = 1, sticky = "W")

mInfoQuantity=Label(mGui, text="Now please enter the amount of items you want to craft.", justify="left")
mInfoQuantity.grid(row = 2, sticky = "W")

mSpinBox = Spinbox(mGui, from_=1, to= 1000, justify="left")
mSpinBox.grid( row = 3, sticky = "W")

mPatternInputButton =Button(mGui, text = "Submit", justify="left", command = mGetPattern)
mPatternInputButton.grid(row=4, sticky = "W")

mLabel2 = Label(mGui, text="Hello there!", anchor="w", justify="left", bg="Green")
mLabel2.grid(row=5,column = 2, sticky= "W")

mListBox = Listbox(mGui, width = 20, height = 8)
mListBox.grid(row=5, sticky = "NW")

mListBox2 = Listbox(mGui, width = 30, height = 20)
mListBox2.grid(row=5,padx = 100,  sticky = "NW")

for item in tradeskills:
    mListBox.insert(END, item)

t = Timer(1, ListBoxChange)
t.start()



mGui.mainloop()
