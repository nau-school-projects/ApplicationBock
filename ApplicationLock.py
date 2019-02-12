from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Application Lock")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# SAVE DESIRED VALUES FOR APP LOCK
WindowToBlock=StringVar() 
TimeDuration=StringVar() 

def search():
  print("The requested app to block is " + WindowToBlock.get())
  print("The requested time to block  is " + TimeDuration.get() + " minutes")
  return ''

ttk.Label(mainframe, text="What Application Would You Like To Lock").grid(column=2, row=1)

ttk.Entry(mainframe, width=7, textvariable=WindowToBlock).grid(column=2, row=2)

ttk.Label(mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=3)

ttk.Entry(mainframe, width=7, textvariable=TimeDuration).grid(column=2, row=4)

ttk.Button(mainframe, text="Engage Lock", command=search).grid(column=2, row=13)


root.mainloop()
