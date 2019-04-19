import unittest
from Scanner import*

class scannerTestCase( unittest.TestCase ): # set up testing class

    # sets up varaibles for every test
    def setUp( self ):
        self.urlReal = "www.facebook.com"
        self.urlFake = "blooforty"
        self.appReal = "find.exe"
        self.appFake = "helloded"

    # Tests to see if a real hostname is added to the dictionary
    def testWebsiteTrue( self ): 
        test = Scanner.addWebsite(self.urlReal, {})
        self.assertEqual( test, 1)

    # Tests to see if a fake hostname isn't added to the dictionary 
    def testWebsiteFalse( self ):
        test = Scanner.addWebsite(self.urlFake, {})
        self.assertEqual( test, 0)

    # tests to see if an executible is added to the dictionary 
    def testAppTrue( self ):
        test = Scanner.addApplication(self.appReal, {})
        self.assertEqual( test, 1)

    # tests to see if a fake executible is not added to the dictionary
    def testAppFalse( self ):
        test = Scanner.addApplication(self.appFake, {})
        self.assertEqual( test, 0)

# runs all tests 
def testScanner():
    unittest.main()
