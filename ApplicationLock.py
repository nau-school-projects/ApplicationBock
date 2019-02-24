from tkinter import *
from tkinter import ttk
import File_Test, time_test, reg_handler

root=Tk()
root.title("Application Lock")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# SAVE DESIRED VALUES FOR APP LOCK
WindowToBlock=StringVar() 
TimeDuration=StringVar() 


def run_locker():
  # Setupworks properly, however application blocking is incorrect in my registry
  # Try to create a registry key that blocks an application whether it be under CurrentVersion\Explorer or
  # under CurrentVersion\Policies
  Editor = reg_handler.Registry_Editor()
  Editor.registry_setup()
  if WindowToBlock.get() == " " or WindowToBlock.get() == "":
    print("No application was selected")
  else:
    print("The string is:", WindowToBlock.get(), ".")
    #reg_handler.add_new_app(WindowToBlock.get(), "1")


  
def search():
  print("The requested app to block is " + WindowToBlock.get())
  print("The requested time to block  is " + TimeDuration.get() + " minutes")
  return ''

ttk.Label(mainframe, text="What Application Would You Like To Lock").grid(column=2, row=1)

ttk.Entry(mainframe, width=7, textvariable=WindowToBlock).grid(column=2, row=2)

ttk.Label(mainframe, text="How Long Would You Like To Block The Application").grid(column=2, row=3)

ttk.Entry(mainframe, width=7, textvariable=TimeDuration).grid(column=2, row=4)

ttk.Button(mainframe, text="Engage Lock", command=run_locker).grid(column=2, row=13)


root.mainloop()
