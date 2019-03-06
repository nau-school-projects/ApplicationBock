# import necessary modules
import os
import winreg

# initialize variables
POLICIES_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies"
EXPLORER_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
DISALLOWRUN_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun"
HKEY = winreg.HKEY_CURRENT_USER

disallowRunKey = None

# algorithm: uses inreg to create the necessary registers for blocking apps on
# windows systems
# precondition: called when the necessary registers to not yet exist
# postcondition: the necessary registers are created
# exceptions: 
def initializeRegistry():

    try:
        # create the necessary registers
        winreg.CreateKey( HKEY, DISALLOWRUN_DIR )
        # create the DisallowRun variable
        explorerKey = winreg.OpenKey( HKEY , EXPLORER_DIR, 0, winreg.KEY_WRITE )
        winreg.SetValueEx( explorerKey, "DisallowRun", 0, winreg.REG_DWORD, 1 )
        winreg.CloseKey( explorerKey )
        
                         
    except WindowsError as error:
        print("Unable to run as an administrator - Could not create registries")
        print(error)             

# algorithm: adds the given app to the
#def addAppToRegistry( str appName ):
    


#def removeAppFromRegistry(str appName ):
    
