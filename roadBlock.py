from random import randint
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Application Lock")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

blockAnswer = IntVar()

def getSolution():
  print("The User Entered", blockAnswer.get())

  if(blockAnswer.get() == product):
    # UNLOCK BUTTON
    # NEED TO LINK THIS BUTTON TO TERMINATION OF TIMER OF LOCK
    Button = ttk.Button(mainframe, text="Unlock", command=getSolution).grid(column=2, row=20)
  return

# CALCULATE ANSWER
valueOne = randint(1, 10)
valueTwo = randint(1, 10)
product = valueOne + valueTwo

# DISPLAY PROMPTS
promptOne = ("Answer This Riddle To Unlock Your System")
promptTwo = ("Add " + str(valueOne) + " and " + str(valueTwo))

# PRINT MATH QUESTION
ttk.Label(mainframe, text=promptOne).grid(column=2, row=1)

ttk.Label(mainframe, text=promptTwo).grid(column=2, row=2)

ttk.Entry(mainframe, width=7, textvariable=blockAnswer).grid(column=2, row=3)

ttk.Button(mainframe, text="Submit", command=getSolution).grid(column=2, row=13)

print("Answer is", product)
 
root.mainloop()






##def unblock():
##    for i in range(user_input):
##        valueOne = randint(1, 10)
##        valueTwo = randint(1, 10)
##        product = valueOne + valueTwo
##        answer = (valueOne, valueTwo)
##
##        if int (answer) == product:
##            button = tk.Button(root, text='Unlock', width=25, command=root.destroy)
##            correct = correct + 1
##
##        else:
##                print("No I'm afraid the answer is %d. \n" %product)
##
## 
##root = tk.Tk()
##root.title("Math Game")
##
##label = tk.Label(root, fg="green")
##label.pack()
##
##tk.Label(mainframe, text="what is " %valueOne %valueTwo).grid(column=2, row=4)
##tk.Entry(root, width=3, textvariable=productValue).grid(column=2, row=5)
##button = tk.Button(root, text='Unlock', width=25, command=root.destroy)
##
##button.pack()
##root.mainloop()
##

        
