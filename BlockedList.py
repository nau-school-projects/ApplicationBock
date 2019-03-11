from WebsiteBlocker import *
from ApplicationBlocker import *

# Simple storage class that holds the a records of all apps/websties entered
# into the app, and whether or not those are blocked. In the future, each
# isntance of the User class will have a unique set of blocked applications,
# hence why this is a class.
class BlockedList( object ):
    # initialize constants
    UNBLOCKED = False
    BLOCKED = True

    def __init__( self ):
        # initialize instance variables

        # Need to choose a Time format we all agree to use
        self.blockedTime = None
        
        # Dictionaries where each key is an app/website found by the Scanner
        # or entered by the User and each value is a constant defining whether
        # the app/website is blocked or not
        self.appDict = {}
        self.webDict = {}
