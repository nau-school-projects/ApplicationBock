import os
import winreg

# Simple storage class that holds the a records of all apps/websties entered
# into the app, and whether or not those are blocked. In the future, each
# isntance of the User class will have a unique set of blocked applications,
# hence why this is a class.
class BlockedList( object ):
    # initialize constants
    UNBLOCKED = False
    BLOCKED = True
    
    # initialize variables
    POLICIES_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies"
    EXPLORER_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
    DISALLOWRUN_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun"
    HKEY = winreg.HKEY_CURRENT_USER
    LOCALHOST = "127.0.0.1"  #defualt local host
    HOSTFILE = r"C:\Windows\System32\Drivers\etc\hosts" #default file path for windows host file

    def __init__( self ):
        # initialize instance variables

        # Need to choose a Time format we all agree to use
        self.blockedTime = None
        
        # Dictionaries where each key is an app/website found by the Scanner
        # or entered by the User and each value is a constant defining whether
        # the app/website is blocked or not
        self.appDict = {}
        self.webDict = {}
        
        
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

    # algorithm: iterates through the app dictionary and adds any blocked apps to
    # the DisallowRun registry, then clears all other values in the registry
    # precondition: passed a dictionary of applications as key and whether they are
    # blocked as values
    # postcondition: any blocked apps are represented in the DisallowRun registry
    # and there are no artifacts in that registry of previous changes
    # exceptions: 
    def updateRegistry( appDict ):
        # initialize funciton/variables
        disallowKey = None
        index = 1

        try:
            # open the disallowrun registry
            disallowKey = winreg.OpenKey( HKEY, DISALLOWRUN_DIR, 0, winreg.KEY_WRITE )

            # loop through appDict
            for app in appDict:

                # if app is blocked, add it
                if( appDict[ app ] == BLOCKED ):

                    winreg.SetValueEx( disallowKey, str( index ), 0, winreg.REG_SZ, app )
                    index += 1
                    
            # end loop

            # clean up any remaining value_name value pairs in the registry

            while( True ):
                winreg.DeleteValue( disallowKey, str( index ) )
                index += 1
                    
        # except value_name not found
        except WindowsError as error:

            # this is the error to be expected if DeleteValue tried to delete
            # something that wasn't there, meaning we are at the end of the
            # registry and can exit
            if( error.winerror == 2 ):
                print( error )
                winreg.CloseKey( disallowKey )
                
                # restart explorer so the changes take effect
                restartExplorer()

                pass

            else:
                if( explorerKey != None ):
                    winreg.CloseKey( explorerKey )
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

    # Takes in a blocked website dictionary and blocks them
    # by adding the website hostnames into system 32 host file
    def blockWebsite( blockedDict ):
        blocked = True
        with open( HOSTFILE, 'r+') as hostFileOpen:
            hostFileContent = hostFileOpen.read()

            for key in blockedDict:
                if key in hostFileContent:
                    pass
                
                else:
                    hostFileOpen.write( LOCALHOST + " " + key + "\n" )
                    
                    blockedDict[key] = blocked

    # Takes the same website dictionary that was blocked
    # and unblockes them by deleting there names from system
    # 32 host file
    def unblockWebsite( blockedDict):
        blocked = False
        with open( HOSTFILE, 'r+') as hostFileOpen:
           
            hostFileContent = hostFileOpen.readlines()

            hostFileOpen.seek(0)

            for line in hostFileContent:
                for key in blockedDict:
                    if not key in line:
                        hostFileOpen.write(line)
                    else:
                        blockedDict[key] = False
                        
            hostFileOpen.truncate()
