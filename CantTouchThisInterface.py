from tkinter import *
from tkinter import ttk
from BlockedList import *
#from timer import *
#from Scanner import *
#from timer import *
## FOR SCHEDULETIMER ##
import schedule
from datetime import datetime

import time
import threading

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

# initialize constants
BLOCK_SCHEDULED = True
BLOCK_NOW = False

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
startTimeStr = StringVar()
stopTimeStr = StringVar()
timerLabel = None
fullList = None


# THREAD

class timerThread( threading.Thread ):
  def __init__( self, firstVal, secondVal, timerLabel, blockType ):
    threading.Thread.__init__(self)
    if(blockType == BLOCK_NOW):
      self.hours = firstVal
      self.minutes = secondVal
    if(blockType == BLOCK_SCHEDULED):
      self.startTime = firstVal
      self.stopTime = secondVal
      self.hours = 0
      self.minutes = 0
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
    hoursDur = int(hoursDur)
    minutesDur = int(minutesDur)

    # formatting time to "xx:xx"
    # if start hour is less than 2 digits, add a leading 0
    if(startTime[0] < 10):
      startHour = "0" + str(startTime[0])
      # if start min is less than 2 digits, add a leading 0
      if(startTime[1] < 10):
        startMin = "0" + str(startTime[1])
        start = str(startHour) + ":" + str(startMin)
      else:
        start = str(startHour) + ":" + str(startTime[1])

    # if stop hour is less than 2 digits, add a leading 0
    if(stopTime[0] < 10):
      stopHour = "0" + str(stopTime[0])
      # if stop min is less than 2 digits, add a leading 0
      if(stopTime[1] < 10):
        stopMin = "0" + str(stopTime[1])
        stop = str(stopHour) + ":" + str(stopMin)
      else:
        stop = str(stopHour) + ":" + str(stopTime[1])

    # if start minute is less than 2 digits but the start hour is not,
    # add a trailing 0 to only the start minute
    if(startTime[0] > 10 and startTime[1] < 10):
      startMin = "0" + str(startTime[1])
      start = str(startTime[0]) + ":" + str(startMin)
    
    # if stop minute is less than 2 digits but the stop hour is not,
    # add a trailing 0 to only the stop minute
    if(stopTime[0] > 10 and stopTime[1] < 10):
      stopMin = "0" + str(stopTime[1])
      stop = str(stopTime[0]) + ":" + str(stopMin)

    # schedule start and end of timer
    schedule.every().day.at(start).do(run, self)
    #schedule.every().day.at(stop).do(exit)
    
    # wait for the scheduled time to run the job
    while True:
      schedule.run_pending()
      time.sleep(1)

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
    newThread = timerThread( numHours.get(), numMinutes.get(), timerLabel, BLOCK_NOW )
    newThread.start()

def activateScheduledTimedBlock():

    # creates tuples for scheduleTimer
    startTuple = createStartTuple(startTimeStr.get())
    stopTuple = createStopTuple(stopTimeStr.get())

    # applications
    blockList.disallowApps( True )
    #updateRegistry( blockList.appDict )
    blockList.updateRegistry()

    # websites
    blockList.blockWebsite()

    # spool off thread to unblock after time is up
    newThread = timerThread( startTuple, stopTuple, timerLabel, BLOCK_SCHEDULED )
    newThread.start()

def createStartTuple(startTimeStr):

    # convert string to tuple
    startTimeStr = str(startTimeStr)
    startTimeList = startTimeStr.split(":")
    startTimeTuple = (startTimeList[0], startTimeList[1])

    # return tuple
    return startTimeTuple

def createStopTuple(stopTimeStr):

    # convert string to tuple
    stopTimeStr = str(stopTimeStr)
    stopTimeList = stopTimeStr.split(":")
    stopTimeTuple = (stopTimeList[0], stopTimeList[1])

    # return tuple
    return stopTimeTuple
  
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

#BUTTON
ttk.Button(mainframe, text="Engage Lock", command=activateTimedBlock).grid(column=2, row=10)

## SCHEDULE TIME TO BE BLOCKED
ttk.Label(mainframe, text="Schedule Time to Block").grid(column=2, row=11)

ttk.Label(mainframe, text="Enter Start Time (24hr, format 'xx:xx')").grid(column=2, row=12)
ttk.Entry(mainframe, width=5, textvariable=startTimeStr).grid(column=2, row=13)

ttk.Label(mainframe, text="Enter Stop Time (24hr, format 'xx:xx')").grid(column=2, row=14)
ttk.Entry(mainframe, width=5, textvariable=stopTimeStr).grid(column=2, row=15)

#BUTTON
ttk.Button(mainframe, text="Engage Scheduled Lock", command=activateScheduledTimedBlock).grid(column=2, row=16)

# APP PIN TO GET DISIRED APPS TO BLOCK
#ttk.Label(mainframe, text="Enter a Pin").grid(column=2, row=5)

#ttk.Entry(mainframe, width=14, textvariable=pinNumber).grid(column=2, row=6)

# BLOCK LEVEL 1-2
#ttk.Label(mainframe, text="Enter Block Level 1 = Minor Block, 2 = Tedious").grid(column=2, row=7)

#ttk.Entry(mainframe, width=14, textvariable=blockLevel).grid(column=2, row=8)

root.mainloop()