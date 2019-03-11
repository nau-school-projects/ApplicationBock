from random import randint
from ApplicationLockInterface import *

from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Locker")
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)



            #GET BLOCK TYPE
# APP PIN TO GET DISIRED APPS TO BLOCK
#get blockLevel
#if(blockLevel == 1)
#SIMPLE POP UP WARNING WINDOW CLICK OK TO CONTINUE
if blockLevel == 1:
    ttk.Label(mainframe, text="are you sure you would like to continue?").grid(column=2, row=5)

    ttk.Button(mainframe, text="Disable Lock").grid(column=2, row=7)

    root.mainloop()




#else
#ANSWER RANDOM MATH PROBLEMS TO CONTINUE

correct = 0  # could be used to determine how many questions needed to complete correctly.

if blockLevel == 2:
    print("You wanted a tedious block! Answer these questions!")
    print("")


    
    for i in range(user_input):
        ttk.Label(mainframe, text="are you sure you would like to continue?").grid(column=2, row=5)

        ttk.Button(mainframe, text="Disable Lock").grid(column=2, row=7)

        root.mainloop()

        num1 = randint(1, 10)
        num2 = randint(1, 10)
        prod = n1 + n2

        ans = input("What's %d added to %d " % (num1, num2))
        if int (ans) == prod:
            
            print("That's right")
            correct = correct + 1
        else:
            print("No I'm afraid the answer is %d. \n" %prod)
        
