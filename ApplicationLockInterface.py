from tkinter import *
from tkinter import ttk
from BlockedList import *
from timer import *

# hacky solution while timer class isn't working
import time

# INITIALIZATION

# initialize BlockedList
# NOTE: in the future, here we need to ask the user to log in, read from
# our file to get their unique BlockedList, and initialize it that way.
blockList = BlockedList()

# initialize window
root=Tk()
root.title("Application Lock")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# initialize variables
appToBlock = StringVar() 
timeDuration = IntVar() # NOTE: Need way to differentiate units user enters
# ideally, user doens't have to type anything and can select number of hours / minutes / seconds
# might not even need seconds, except for teting purposes
pinNumber = StringVar()
blockLevel = StringVar()

# FUNCTIONS
def search():
  print("The requested app to block is " + appToBlock.get())
  print("The requested time to block  is " + timeDuration.get() + " minutes")
  print("Optional: create a Pin # for lock recent " + pinNumber.get() + " minutes")
  print("The requested block level is " + blockLevel.get())
  return ''

def addApp():
  blockList.appDict[ appToBlock.get() ] = BLOCKED


def activateTimedBlock():
  disallowApps( True )
  updateRegistry( blockList.appDict )
  # for now, pasing it a bogus unit so that it will default to seconds
  #run_timer( timeDuration.get(), "Noot noot", disallowApps( False ) )
  time.sleep( timeDuration.get() )
  disallowApps( False )
  

# WINDOW

# ADD APP TO BE BLOCKED
ttk.Label(mainframe, text="What Application Would You Like To Lock").grid(column=2, row=1)

ttk.Entry(mainframe, width=7, textvariable=appToBlock).grid(column=2, row=2)

# ADD APP BUTTON
ttk.Button(mainframe, text="Add", command=addApp).grid(column=3, row=2)

# TIME TO BE BLOCKED FOR
ttk.Label(mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=3)

ttk.Entry(mainframe, width=7, textvariable=timeDuration).grid(column=2, row=4)

# APP PIN TO GET DISIRED APPS TO BLOCK
ttk.Label(mainframe, text="Enter a Pin").grid(column=2, row=5)

ttk.Entry(mainframe, width=7, textvariable=pinNumber).grid(column=2, row=6)

# BLOCK LEVEL 1-2
ttk.Label(mainframe, text="Enter Block Level 1 = Minor Block, 2 = Tedious").grid(column=2, row=7)

ttk.Entry(mainframe, width=7, textvariable=blockLevel).grid(column=2, row=8)

#BUTTON
ttk.Button(mainframe, text="Engage Lock", command=activateTimedBlock).grid(column=2, row=13)


root.mainloop()











