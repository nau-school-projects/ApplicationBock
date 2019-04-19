from tkinter import *
from tkinter import ttk
from BlockedList import *
from UserManager import *
from timer import *
#from Scanner import *

import schedule
from datetime import datetime

import time
import threading

# initialize constants for type of block
BLOCK_SCHEDULED = True
BLOCK_NOW = False

class MainWindow:

  # THREAD

  # timerThread class
  class timerThread( threading.Thread ):
    
    # initalize the timer thread
    def __init__( self, firstVal, secondVal, blockList, timerLabel, blockType ):
      
      threading.Thread.__init__(self)

      self.blockList = blockList
      self.timerLabel = timerLabel
      self.blockType = blockType
      
      # block will engage immediately
      if( blockType == BLOCK_NOW ):
        self.hours = firstVal
        self.minutes = secondVal

      # block was scheduled
      if( blockType == BLOCK_SCHEDULED ):
        self.startTime = firstVal
        self.stopTime = secondVal
        self.hours = 0
        self.minutes = 0

    # function called when thread is started
    # will split to appropriate behavior based on flag passed
    def run( self ):
      if( self.blockType == BLOCK_NOW ):
        self.runTimer()
      else:
        self.scheduleTimer()

    # Function: runTimer
    # Desc: Utilizes time.sleep to run a timer
    def runTimer( self ):
      
      # initalizing variables
      hours = self.hours
      minutes = self.minutes;
      seconds = 0
      timerLabel = self.timerLabel

      # block everything
      self.blockList.disallowApps( True )
      self.blockList.updateRegistry()
      self.blockList.blockWebsite()

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
      self.blockList.disallowApps( False )
      self.blockList.unblockWebsite()

    # Function: scheduleTimer
    # Desc: schedules the runTimer method to run during
    #       passed in intervals
    def scheduleTimer(self):

      # initialization
      startTime = self.startTime
      stopTime = self.stopTime
      hoursDur = self.hours
      minutesDur = self.minutes

      # initialize variables and format them to ("xx:xx")
      start = str(startTime[0]) + ":" + str(startTime[1])
      stop = str(stopTime[0]) + ":" + str(stopTime[1])

      # calculate duration between start and stop time
      timeFormat = "%H:%M"
      timeDelta = datetime.strptime(stop, timeFormat) - datetime.strptime(start, timeFormat)

      # split the timeDelta into hours, minutes, and seconds variables for runTimer
      hoursDur, minutesDur, secondsDur = str(timeDelta).split(":")
      if(hoursDur != "0"):
        hoursDur = hoursDur.lstrip("0")
      if(minutesDur != "0"):
        minutesDur = minutesDur.lstrip("0")
      # converting string to int
      self.hours = int(hoursDur)
      self.minutes = int(minutesDur)
      
      # formatting time to "xx:xx"
      # if start hour is less than 2 digits, add a leading 0
      if(int(startTime[0]) < 10):
        tempStartHr = str(startTime[0])
        tempStartHr = tempStartHr.lstrip("0")
        startHour = "0" + str(tempStartHr)
        # if start min is less than 2 digits, add a leading 0
        if(int(startTime[1]) < 10):
          tempStartMin = str(startTime[1])
          tempStartMin = tempStartMin.lstrip("0")
          startMin = "0" + str(tempStartMin)
          if(startMin == "0"):
            startMin = "0" + startMin
          start = str(startHour) + ":" + str(startMin)
        else:
          start = str(startHour) + ":" + str(startTime[1])

      # if stop hour is less than 2 digits, add a leading 0
      if(int(stopTime[0]) < 10):
        tempStopHr = str(stopTime[0])
        tempStopHr = tempStopHr.lstrip("0")
        stopHour = "0" + str(tempStopHr)
        # if stop min is less than 2 digits, add a leading 0
        if(int(stopTime[1]) < 10):
          tempStopMin = str(stopTime[1])
          tempStopMin = tempStopMin.lstrip("0")
          stopMin = "0" + str(tempStopMin)
          if(stopMin == "0"):
            stopMin = "0" + stopMin
          stop = str(stopHour) + ":" + str(stopMin)
        else:
          stop = str(stopHour) + ":" + str(stopTime[1])

      # if start minute is less than 2 digits but the start hour is not,
      # add a trailing 0 to only the start minute
      if(int(startTime[0]) > 10 and int(startTime[1]) < 10):
        tempStartMin = str(startTime[1])
        tempStartMin = tempStartMin.lstrip("0")
        startMin = "0" + str(tempStartMin)
        if(startMin == "0"):
          startMin = "0" + startMin
        start = str(startTime[0]) + ":" + str(startMin)
      
      # if stop minute is less than 2 digits but the stop hour is not,
      # add a trailing 0 to only the stop minute
      if(int(stopTime[0]) > 10 and int(stopTime[1]) < 10):
        tempStopMin = str(stopTime[1])
        tempStopMin = tempStopMin.lstrip("0")
        stopMin = "0" + str(tempStopMin)
        if(stopMin == "0"):
          stopMin = "0" + stopMin
        stop = str(stopTime[0]) + ":" + str(stopMin)

      # schedule start and end of timer
      schedule.every().day.at(start).do(self.runTimer)
      # schedule.every().day.at(stop).do(exit)

      # wait for the scheduled time to run the job
      while True:
        schedule.run_pending()
        time.sleep(1)
  

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
    self.numMinutes = IntVar()
    self.numHours = IntVar()
    self.startTimeStr = StringVar()
    self.stopTimeStr = StringVar()
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

    #BUTTON
    ttk.Button(self.mainframe, text="Engage Lock", command=self.activateTimedBlock).grid(column=2, row=10)

     ## SCHEDULE TIME TO BE BLOCKED
    ttk.Label(self.mainframe, text="Schedule Time to Block").grid(column=2, row=11)

    # ENTER START TIME
    ttk.Label(self.mainframe, text="Enter Start Time (24hr, format 'xx:xx')").grid(column=2, row=12)
    ttk.Entry(self.mainframe, width=5, textvariable=self.startTimeStr).grid(column=2, row=13)

    # ENTER STOP TIME
    ttk.Label(self.mainframe, text="Enter Stop Time (24hr, format 'xx:xx')").grid(column=2, row=14)
    ttk.Entry(self.mainframe, width=5, textvariable=self.stopTimeStr).grid(column=2, row=15)

    # BUTTON TO ENGAGE A SCHEDULED LOCK
    ttk.Button(self.mainframe, text="Engage Scheduled Lock", command=self.activateScheduledTimedBlock).grid(column=2, row=16)

    

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

  def createStartTuple( self, startTimeStr ):

    # convert string to tuple
    startTimeStr = str(startTimeStr)
    startTimeList = startTimeStr.split(":")
    startTimeTuple = (startTimeList[0], startTimeList[1])

    # return tuple
    return startTimeTuple

  def createStopTuple(self, stopTimeStr):

    # convert string to tuple
    stopTimeStr = str(stopTimeStr)
    stopTimeList = stopTimeStr.split(":")
    stopTimeTuple = (stopTimeList[0], stopTimeList[1])

    # return tuple
    return stopTimeTuple

  def activateTimedBlock( self ):

    # spool off thread to block, then unblock after time is up
    newThread = self.timerThread( self.numHours.get(), self.numMinutes.get(), self.blockList, self.timerLabel, BLOCK_NOW )
    newThread.start()

  def activateScheduledTimedBlock( self ):

    # creates tuples for scheduleTimer (formatting)
    startTuple = self.createStartTuple(self.startTimeStr.get())
    stopTuple = self.createStopTuple(self.stopTimeStr.get())

    # spool off thread to block, then unblock after time is up
    newThread = self.timerThread( startTuple, stopTuple, self.blockList, self.timerLabel, BLOCK_SCHEDULED )
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











