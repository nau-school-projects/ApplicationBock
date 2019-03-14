from tkinter import *
from tkinter import ttk
from BlockedList import *
from timer import *
from Scanner import *

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
mainframe.pack(fill=None, expand=False)

# initialize variables
appToBlock = StringVar()
websiteToBlock = StringVar()
timeDuration = IntVar() # NOTE: Need way to differentiate units user enters
# ideally, user doens't have to type anything and can select number of hours / minutes / seconds
# might not even need seconds, except for teting purposes
pinNumber = StringVar()
blockLevel = StringVar()
numMinutes=StringVar()
numHours=StringVar()
fullList = None

# FUNCTIONS
def search():
  print("The requested app to block is " + appToBlock.get())
  print("The requested time to block  is " + timeDuration.get() + " minutes")
  print("Optional: create a Pin # for lock recent " + pinNumber.get() + " minutes")
  print("The requested block level is " + blockLevel.get())
  print("Number of hours to block the application " + numHours.get() + " hours")
  print("Number of minutes to block the application" + numMinutes.get() + "hours")
  return ''

def addApp():
  blockList.appDict[ appToBlock.get() ] = BLOCKED
  
  currentList = fullList[ "text" ]
  currentList += ( appToBlock.get() + " - " + "BLOCKED\n" )
  fullList[ "text" ] = currentList

def addWebsite():
  blockList.webDict[ websiteToBlock.get() ] = BLOCKED

  currentList = fullList[ "text" ]
  currentList += ( websiteToBlock.get() + " - " + "BLOCKED\n" )
  fullList[ "text" ] = currentList

def activateTimedBlock():

  # applications
  disallowApps( True )
  updateRegistry( blockList.appDict )

  # websites
  blockWebsite( blockList.webDict )

  # unblock
  # for now, pasing it a bogus unit so that it will default to seconds
  run_sleep_timer( timeDuration.get(), "Time Unit" )
  disallowApps( False )
  unblockWebsite( blockList.webDict )

# WINDOW

# ADD APP TO BE BLOCKED
ttk.Label(mainframe, text="What Application Would You Like To Lock").grid(column=2, row=1)

ttk.Entry(mainframe, width=21, textvariable=appToBlock).grid(column=2, row=2)

# ADD APP BUTTON
ttk.Button(mainframe, text="Add", command=addApp).grid(column=3, row=2)

# ADD WEBSITE TO BE BLOCKED
ttk.Label(mainframe, text="What Website Would You Like To Lock").grid(column=2, row=3)

ttk.Entry(mainframe, width=21, textvariable=websiteToBlock).grid(column=2, row=4)

# ADD WEBSITE BUTTON
ttk.Button(mainframe, text="Add", command=addWebsite).grid(column=3, row=4)

# LIST OF APPS/WEBSITE
fullList = ttk.Label(mainframe, text="",)
fullList.grid(column=4, row=1)

## TIME TO BE BLOCKED FOR
ttk.Label(mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=3)

ttk.Label(mainframe, text="Enter Hours").grid(column=2, row=4)
ttk.Entry(mainframe, width=3, textvariable=numHours).grid(column=2, row=5)

ttk.Label(mainframe, text="Enter Minutes").grid(column=2, row=6)
ttk.Entry(mainframe, width=3, textvariable=numMinutes).grid(column=2, row=7)

# APP PIN TO GET DISIRED APPS TO BLOCK
#ttk.Label(mainframe, text="Enter a Pin").grid(column=2, row=5)

#ttk.Entry(mainframe, width=14, textvariable=pinNumber).grid(column=2, row=6)

# BLOCK LEVEL 1-2
#ttk.Label(mainframe, text="Enter Block Level 1 = Minor Block, 2 = Tedious").grid(column=2, row=7)

#ttk.Entry(mainframe, width=14, textvariable=blockLevel).grid(column=2, row=8)

#BUTTON
ttk.Button(mainframe, text="Engage Lock", command=activateTimedBlock).grid(column=2, row=13)


root.mainloop()
