from tkinter import *
from tkinter import ttk
from BlockedList import *
#from timer import *
#from Scanner import *
from timer import *

import time
import threading

# INITIALIZATION

# initialize BlockedList
# NOTE: in the future, here we need to ask the user to log in, read from
# our file to get their unique BlockedList, and initialize it that way.
blockList = BlockedList()

# initialize window
root=Tk()
root.title("Can't Touch This")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(fill=None, expand=False)

# initialize variables
appToBlock = StringVar()
websiteToBlock = StringVar()
pinNumber = StringVar()
blockLevel = StringVar()
# NOTE: Need way to differentiate units user enters
# ideally, user doens't have to type anything and can select number of hours / minutes / seconds
# might not even need seconds, except for teting purposes
numMinutes=IntVar()
numHours=IntVar()
timerLabel = None
fullList = None


# THREAD

class timerThread( threading.Thread ):
  def __init__( self, hours, minutes, timerLabel ):
    threading.Thread.__init__(self)
    self.hours = hours
    self.minutes = minutes
    self.timerLabel = timerLabel

  def run(self):
    # initalizing variables
    hours = self.hours
    minutes = self.minutes;
    seconds = 0
    timerLabel = self.timerLabel

    # calculate total duration in seconds
    duration = int(( hours * 3600 ) + ( minutes * 60 ))

    # iterate through duration ( 0 to duration )
    for i in range(duration):
      if seconds == 0:
        if minutes != 0:
          minutes = minutes - 1
          seconds = 60
      if minutes == 0:
        if hours != 0:
          hours = hours - 1
          minutes = 59
          seconds = 60

      # decremenet seconds
      seconds = seconds - 1

      # wait for 1 second
      time.sleep(1)

      # output current timer countdown
      currentList = timerLabel[ "text" ]
      currentList = ( hours, ":", minutes, ":", seconds )
      timerLabel[ "text" ] = currentList

    # time is up, unblock everything
    timerLabel[ "text" ] = ""
    blockList.disallowApps( False )
    blockList.unblockWebsite()

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
    blockList.disallowApps( True )
    #updateRegistry( blockList.appDict )
    blockList.updateRegistry()

    # websites
    blockList.blockWebsite()

    # spool off thread to unblock after time is up
    newThread = timerThread( numHours.get(), numMinutes.get(), timerLabel )
    newThread.start()
  
# WINDOW

# TIMER
timerLabel = ttk.Label(mainframe, text="")
timerLabel.grid(column=1, row=1)

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
fullList = ttk.Label(mainframe, text="")
#fullList = Text(mainframe, height=10, width=30, state=DISABLED)
fullList.grid(column=4, row=1, rowspan = 10, sticky = N+S)

## TIME TO BE BLOCKED FOR
ttk.Label(mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=5)

ttk.Label(mainframe, text="Enter Hours").grid(column=2, row=6)
ttk.Entry(mainframe, width=5, textvariable=numHours).grid(column=2, row=7)

ttk.Label(mainframe, text="Enter Minutes").grid(column=2, row=8)
ttk.Entry(mainframe, width=5, textvariable=numMinutes).grid(column=2, row=9)

# APP PIN TO GET DISIRED APPS TO BLOCK
#ttk.Label(mainframe, text="Enter a Pin").grid(column=2, row=5)

#ttk.Entry(mainframe, width=14, textvariable=pinNumber).grid(column=2, row=6)

# BLOCK LEVEL 1-2
#ttk.Label(mainframe, text="Enter Block Level 1 = Minor Block, 2 = Tedious").grid(column=2, row=7)

#ttk.Entry(mainframe, width=14, textvariable=blockLevel).grid(column=2, row=8)

#BUTTON
ttk.Button(mainframe, text="Engage Lock", command=activateTimedBlock).grid(column=2, row=13)


root.mainloop()











