# import necessary modules
import os
import winreg

# initialize variables
POLICIES_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies"
EXPLORER_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
DISALLOWRUN_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun"
HKEY = winreg.HKEY_CURRENT_USER

# algorithm: uses inreg to create the necessary registers for blocking apps on
# windows systems
# precondition: called when the necessary registers to not yet exist
# postcondition: the necessary registers are created
# exceptions: 
def initializeRegistry():

    # initialize function/variables
    explorerKey = None

    try:
        # create the necessary registers
        winreg.CreateKey( HKEY, DISALLOWRUN_DIR )
        # create the DisallowRun variable
        explorerKey = winreg.OpenKey( HKEY , EXPLORER_DIR, 0, winreg.KEY_WRITE )
        winreg.SetValueEx( explorerKey, "DisallowRun", 0, winreg.REG_SZ, "1" )
        winreg.CloseKey( explorerKey )
        
                         
    except WindowsError as error:
        if( explorerKey != None ):
            winreg.CloseKey( explorerKey )
        print("Unable to run as an administrator - Could not create registries")
        print(error)             

# algorithm: application the given app to the DisallowRun registry
# precondition: passed application name as a string and its associated ID number as a string
# postcondition: a value name/value pair is added to the DisallowRun registry
# of the form ID/application name
# exceptions:
def addAppToRegistry( appName, regNum ):

    # initialize function/variables
    disallowKey = None

    try:
        # write application name to the registry
        disallowKey = winreg.OpenKey( HKEY, DISALLOWRUN_DIR, 0, winreg.KEY_WRITE )
        winreg.SetValueEx( disallowKey, regNum, 0, winreg.REG_SZ, appName ) 
        winreg.CloseKey( disallowKey )

        # restart explorer so the changes take effect
        restartExplorer()
    
    except WindowsError as error:
        if( disallowKey != None ):
            winreg.CloseKey( disallowKey )
        print("Unable to run as an administrator - Could not create registries")
        print(error)    

# algorithm: removes an application from the DisallowRun registry
# precondition: passed the ID number of the target app as a string
# postcondition: value name/value pair with the passed ID is no longer in the
# DisalloRun registry
# exceptions:
def removeAppFromRegistry( regNum ):
    # initialize function/variables
    disallowKey = None

    try:
        # write application name to the registry
        disallowKey = winreg.OpenKey( HKEY, DISALLOWRUN_DIR, 0, winreg.KEY_WRITE )
        winreg.DeleteValue( disallowKey, appName ) 
        winreg.CloseKey( disallowKey )

        # restart explorer so the changes take effect
        restartExplorer()
    
    except WindowsError as error:
        if( disallowKey != None ):
            winreg.CloseKey( disallowKey )
        print("Unable to run as an administrator - Could not create registries")
        print(error)

# algorithm: sets the DisallowRun value in the Explorer key to:
# "1" - disables applications in the DisallowRun key
# "" - enables applciations in the DisallowRun key
# precondition: passed True or False indicating whether the value should be set
# to "1" or "" respectively
# postcondition: the DisallowRun value is changed to the indicated string
# exceptions:
def disallowApps( disallow ):

    # initialize function/variables
    explorerKey = None
    disallowValue = None

    if( disallow ):
        disallowValue = "1"
    else:
        disallowValue = ""

    try:
        # write application name to the registry
        explorerKey = winreg.OpenKey( HKEY, EXPLORER_DIR, 0, winreg.KEY_WRITE )
        winreg.SetValueEx( explorerKey, "DisallowRun", 0, winreg.REG_SZ, disallowValue ) 
        winreg.CloseKey( explorerKey )

        # restart explorer so the changes take effect
        restartExplorer()
    
    except WindowsError as error:
        if( explorerKey != None ):
            winreg.CloseKey( explorerKey )
        print("Unable to run as an administrator - Could not create registries")
        print(error)

# algorithm: utility function that runs windows shell commands to restart
# Windows Explorer so change made to the registry will take effect
# precondition: 
# postcondition:
# exceptions:
def restartExplorer():
    # initialize function/variables
    cmd = ""

    # run commnds
    cmd = "taskkill /f /IM explorer.exe"
    os.system( cmd )
    cmd = "start explorer.exe"
    os.system( cmd )
    cmd = "exit"
    os.system( cmd )
    
    
