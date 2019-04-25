import unittest
from BlockedList import *
import ctypes

class SimpleTestCase( unittest.TestCase ):

    def testA( self ):
        """Test case A. Tests BlockedList modifying registers"""

        #assert sys.argv[-1] == ASADMIN, "BlockedList must be run as administrator to function"

        # test to see if running as admin 
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if not is_admin:
            self.fail("BlockedList must be run as admin to function")
        
        blockListA = BlockedList()
        blockListA.appDict["appA"] = BLOCKED
        blockListA.appDict["appB"] = BLOCKED
        blockListA.appDict["appC"] = BLOCKED
        blockListA.appDict["appD"] = UNBLOCKED

        blockListA.updateRegistry()

        assert blockListA.keyIsPresent( "appA" ), "disallowRun registry not being correctly set"
        assert blockListA.keyIsPresent( "appB" ), "disallowRun registry not being correctly set"
        assert blockListA.keyIsPresent( "appC" ), "disallowRun registry not being correctly set"
        assert blockListA.keyIsPresent( "appD" ) == False, "disallowRun registry not being correctly set"
        
        blockListA.disallowApps( True )

        assert blockListA.appsAreBlocked(), "disallowApps not correctly modifying explorer registry"

        blockListA.disallowApps( False )

        assert blockListA.appsAreBlocked() == False, "disallowApps not correctly modifying explorer registry"

# run all tests
if __name__ == "__main__":
    unittest.main()
