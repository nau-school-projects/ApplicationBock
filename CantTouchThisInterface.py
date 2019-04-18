from tkinter import *
from tkinter import ttk
from BlockedList import *
from UserManager import *
from timer import *
#from Scanner import *

import time
import threading

class MainWindow:

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
  

  def __init__( self, root, userManager ):
    # initialize variables
    
    # initialize BlockedList
    # NOTE: in the future, here we need to ask the user to log in, read from
    # our file to get their unique BlockedList, and initialize it that way.
    self.blockList = BlockedList()
    self.appToBlock = StringVar()
    self.websiteToBlock = StringVar()
    self.blockLevel = StringVar()
    # NOTE: Need way to differentiate units user enters
    # ideally, user doens't have to type anything and can select number of hours / minutes / seconds
    # might not even need seconds, except for teting purposes
    self.numMinutes=IntVar()
    self.numHours=IntVar()
    self.timerLabel = None
    self.fullList = None    

    # create window
    self.root=root
    self.root.title("Can't Touch This")
    self.mainframe = ttk.Frame(self.root, padding="10 10 12 12")
    self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    self.mainframe.columnconfigure(0, weight=1)
    self.mainframe.rowconfigure(0, weight=1)
    self.mainframe.pack(fill=None, expand=False)

    # WINDOW

    # TIMER
    self.timerLabel = ttk.Label(self.mainframe, text="")
    self.timerLabel.grid(column=1, row=1)

    # ADD APP TO BE BLOCKED
    ttk.Label(self.mainframe, text="What Application Would You Like To Lock").grid(column=2, row=1)

    ttk.Entry(self.mainframe, width=21, textvariable=self.appToBlock).grid(column=2, row=2)

    # ADD APP BUTTON
    ttk.Button(self.mainframe, text="Add", command=self.addApp).grid(column=3, row=2)

    # ADD WEBSITE TO BE BLOCKED
    ttk.Label(self.mainframe, text="What Website Would You Like To Lock").grid(column=2, row=3)

    ttk.Entry(self.mainframe, width=21, textvariable=self.websiteToBlock).grid(column=2, row=4)

    # ADD WEBSITE BUTTON
    ttk.Button(self.mainframe, text="Add", command=self.addWebsite).grid(column=3, row=4)

    # LIST OF APPS/WEBSITE
    self.fullList = ttk.Label(self.mainframe, text="")
    #fullList = Text(mainframe, height=10, width=30, state=DISABLED)
    self.fullList.grid(column=4, row=1, rowspan = 10, sticky = N+S)

    ## TIME TO BE BLOCKED FOR
    ttk.Label(self.mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=5)

    ttk.Label(self.mainframe, text="Enter Hours").grid(column=2, row=6)
    ttk.Entry(self.mainframe, width=5, textvariable=self.numHours).grid(column=2, row=7)

    ttk.Label(self.mainframe, text="Enter Minutes").grid(column=2, row=8)
    ttk.Entry(self.mainframe, width=5, textvariable=self.numMinutes).grid(column=2, row=9)

    # BLOCK LEVEL 1-2
    #ttk.Label(mainframe, text="Enter Block Level 1 = Minor Block, 2 = Tedious").grid(column=2, row=7)

    #ttk.Entry(mainframe, width=14, textvariable=blockLevel).grid(column=2, row=8)

    #BUTTON
    ttk.Button(self.mainframe, text="Engage Lock", command=self.activateTimedBlock).grid(column=2, row=13)

  # FUNCTIONS
  def search( self ):
    print("The requested app to block is " + appToBlock.get())
    print("The requested time to block  is " + timeDuration.get() + " minutes")
    print("Optional: create a Pin # for lock recent " + pinNumber.get() + " minutes")
    print("The requested block level is " + blockLevel.get())
    print("Number of hours to block the application " + numHours.get() + " hours")
    print("Number of minutes to block the application" + numMinutes.get() + "hours")
    return ''

  def addApp( self ):
    self.blockList.appDict[ self.appToBlock.get() ] = BLOCKED
    
    self.currentList = self.fullList[ "text" ]
    self.currentList += ( self.appToBlock.get() + " - " + "BLOCKED\n" )
    self.fullList[ "text" ] = self.currentList

  def addWebsite( self ):
    self.blockList.webDict[ self.websiteToBlock.get() ] = BLOCKED

    self.currentList = self.fullList[ "text" ]
    self.currentList += ( self.websiteToBlock.get() + " - " + "BLOCKED\n" )
    self.fullList[ "text" ] = self.currentList

  def activateTimedBlock( self ):
      # applications
      self.blockList.disallowApps( True )
      #updateRegistry( blockList.appDict )
      self.blockList.updateRegistry()

      # websites
      self.blockList.blockWebsite()

      # spool off thread to unblock after time is up
      newThread = self.timerThread( self.numHours.get(), self.numMinutes.get(), self.timerLabel )
      newThread.start()


class LoginWindow:
  
  def __init__( self, root, userManager ):
    # initialize variables
    
    # initialize BlockedList
    # NOTE: in the future, here we need to ask the user to log in, read from
    # our file to get their unique BlockedList, and initialize it that way.
    self.userManager = userManager
    self.username = StringVar()
    self.password = StringVar()
    self.message = None
    
    # create window
    self.root=root
    self.root.title("Can't Touch This")
    self.mainframe = ttk.Frame(self.root, padding="10 10 12 12")
    self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    self.mainframe.columnconfigure(0, weight=1)
    self.mainframe.rowconfigure(0, weight=1)
    self.mainframe.pack(fill=None, expand=False)

    # WINDOW

    # USERNAME
    ttk.Label(self.mainframe, text="Username").grid(column=2, row=1)

    ttk.Entry(self.mainframe, width=21, textvariable=self.username).grid(column=2, row=2)

    # PASSWORD
    ttk.Label(self.mainframe, text="Password").grid(column=2, row=3)

    ttk.Entry(self.mainframe, width=21, show="*", textvariable=self.password).grid(column=2, row=4)

    # MESSAGE
    self.message = ttk.Label(self.mainframe, text="").grid(column=2, row=5)
    #self.message.grid(column=2, row=5)

    # LOGIN
    ttk.Button(self.mainframe, text="Add", command=self.login).grid(column=2, row=6)

  def login( self ):
    selectedProfile = self.userManager.checkPassword( self.username.get(), self.password.get() )
    if selectedProfile != None:
      MainWindow( self.root )
    else:
      self.message[ "text" ] = "username or password is incorrect"

def main():

    # here we initialzie the UserManager (this also could be done in a seperate Main class, but I dunno)
    # read the file to set up the UserManager
    # if there is no file/if the file is empty the UserManager should be empty and go straight to the main window
    userManager = UserManager()
  
    root = Tk()
    #app = MainWindow(root)

    # check if the dictionary is empty - meaning that a file wasn't able to be
    # loaded and there are no user profiles
    # empty dictionaries will evaluate to false
    if( userManager.usersDict ):
      app = LoginWindow( root, userManager )
    else:
      app = MainWindow( root, userManager )
      
    root.mainloop()

if __name__ == '__main__':
    main()











