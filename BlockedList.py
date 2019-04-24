# import necessary modules
import os
import winreg

# initialize constants
UNBLOCKED = False
BLOCKED = True

POLICIES_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies"
EXPLORER_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
DISALLOWRUN_DIR = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun"
HKEY = winreg.HKEY_CURRENT_USER

LOCALHOST = "127.0.0.1"  #defualt local host
HOSTFILE = r"C:\Windows\System32\Drivers\etc\hosts" #default file path for windows host file

# Simple storage class that holds the a records of all apps/websties entered
# into the app, and whether or not those are blocked. In the future, each
# isntance of the User class will have a unique set of blocked applications,
# hence why this is a class.
class BlockedList( object ):

    def __init__( self ):
        # initialize instance variables

        # Need to choose a Time format we all agree to use
        self.blockedTime = None
        
        # Dictionaries where each key is an app/website found by the Scanner
        # or entered by the User and each value is a constant defining whether
        # the app/website is blocked or not
        self.appDict = {}
        self.webDict = {}

    # algorithm: iterates through the app dictionary and adds any blocked apps to
    # the DisallowRun registry, then clears all other values in the registry
    # precondition: passed a dictionary of applications as key and whether they are
    # blocked as values
    # postcondition: any blocked apps are represented in the DisallowRun registry
    # and there are no artifacts in that registry of previous changes
    # exceptions: 
    def updateRegistry( self ):
        # initialize funciton/variables
        disallowKey = None
        index = 1

        try:
            # open the disallowrun registry
            disallowKey = winreg.OpenKey( HKEY, DISALLOWRUN_DIR, 0, winreg.KEY_WRITE )

            # loop through appDict
            for app in self.appDict:

                # if app is blocked, add it
                if( self.appDict[ app ] == BLOCKED ):

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
                self.restartExplorer()

                pass

            else:
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
    def disallowApps( self, disallow ):

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
            self.restartExplorer()
        
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
    def restartExplorer( self ):
        # initialize function/variables
        cmd = ""

        # run commnds
        cmd = "taskkill /f /IM explorer.exe"
        os.system( cmd )
        cmd = "start explorer.exe"
        os.system( cmd )
        cmd = "exit"
        os.system( cmd )

    def blockWebsite( self ):
        blocked = True
        with open( HOSTFILE, 'r+') as hostFileOpen:
            hostFileContent = hostFileOpen.read()

            for key in self.webDict:
                if key in hostFileContent:
                    pass
                
                else:
                    hostFileOpen.write( LOCALHOST + " " + key + "\n" )
                    
                    self.webDict[key] = blocked
        return 0

    def unblockWebsite( self ):
        blocked = False
        with open( HOSTFILE, 'r+') as hostFileOpen:
           
            hostFileContent = hostFileOpen.readlines()

            hostFileOpen.seek(0)

            for line in hostFileContent:
                for key in self.webDict:
                    if not key in line:
                        hostFileOpen.write(line)
                    else:
                        self.webDict[key] = False
                        
            hostFileOpen.truncate()
            
        return 0

