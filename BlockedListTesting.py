import unittest
from BlockedList import*

class BlockedListTestCases( unittest.TestCase ): # set up testing class

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

# runs all tests 
def testBlockedList():
    unittest.main()
