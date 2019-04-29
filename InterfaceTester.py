import unittest
from ApplicationLockInterface import *

class interfaceTest(unittest.TestCase):

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

 

if __name__ == '__main__':
    unittest.main()


## def setUp( self ):
##        self.urlReal = "www.facebook.com"
##        self.urlFake = "blooforty"
##        self.appReal = "find.exe"
##        self.appFake = "helloded"
##
##    # Testing to make sure that website blocker runs all the way through
##    def testWebsiteBlock( self ): 
##        test = BlockedList.blockWebsite()
##        self.assertEqual( test, 0)
##
##    # Website unblocker should run through no matter what! Testing this!
##    def testWebsiteUnblock( self ):
##        test = BlockedList.unblockWebsite()
##        self.assertEqual( test, 0)
