from ApplicationLockInterface_2.0 import *
import unittest
from BlockedList import *
import ctypes

class BlockedListTestCases( unittest.TestCase ):
    ###########################################################
    #Ensure values can be stored into user interface
    def testApp(self):
        self.assertEqual(appEntered("slack"), "slack") 

    def testWebsite(self):
        self.assertEqual(websiteEntered("facebook"), "facebook") 

    def testPin(self):
        self.assertEqual(pinNumberEntered(10113), 10113) 

    def testLevel(self):
        self.assertEqual(blockLevelEntered(1), 1) 

    def testMinutes(self):
        self.assertEqual(numMinutesEntered(10), 10) 

    def testHours(self):
        self.assertEqual(numHoursEntered(1), 1)  
    ###########################################################
        
    # sets up varaibles for every test
    def setUp( self ):
        self.urlReal = "www.facebook.com"
        self.urlFake = "blooforty"
        self.appReal = "find.exe"
        self.appFake = "helloded"

    # Testing to make sure that website blocker runs all the way through
    def testWebsiteBlock( self ): 
        test = BlockedList.blockWebsite()
        self.assertEqual( test, 0)

    # Website unblocker should run through no matter what! Testing this!
    def testWebsiteUnblock( self ):
        test = BlockedList.unblockWebsite()
        self.assertEqual( test, 0)

    # Test that applicaiton blocker correctly modifies registries
    def testApplicationBlocker( self ):
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

 

if __name__ == '__main__':
    unittest.main()
