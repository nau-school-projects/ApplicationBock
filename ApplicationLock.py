from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Application Lock")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# SAVE DESIRED VALUES FOR APP LOCK
windowToBlock=StringVar() 
timeDuration=StringVar()
pinNumber=StringVar()
blockLevel = StringVar()

def search():
  print("The requested app to block is " + windowToBlock.get())
  print("The requested time to block  is " + timeDuration.get() + " minutes")
  print("Optional: create a Pin # for lock recent " + pinNumber.get() + " minutes")
  return ''

# APP TO BE BLOCKED
ttk.Label(mainframe, text="What Application Would You Like To Lock").grid(column=2, row=1)

ttk.Entry(mainframe, width=7, textvariable=windowToBlock).grid(column=2, row=2)

# TIME TO BE BLOCKED FOR
ttk.Label(mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=3)

ttk.Entry(mainframe, width=7, textvariable=timeDuration).grid(column=2, row=4)

# APP PIN TO GET DISIRED APPS TO BLOCK
ttk.Label(mainframe, text="Enter a Pin").grid(column=2, row=5)

ttk.Entry(mainframe, width=7, textvariable=pinNumber).grid(column=2, row=6)

ttk.Label(mainframe, text="Enter Block Level 1 = Minor Block, 2 = Tedious").grid(column=2, row=7)

ttk.Entry(mainframe, width=7, textvariable=blockLevel).grid(column=2, row=8)

ttk.Button(mainframe, text="Engage Lock", command=search).grid(column=2, row=13)


root.mainloop()











