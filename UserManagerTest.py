import unittest
from UserManager import *
from BlockedList import *



class SimpleTestCase( unittest.TestCase ):

    def testA( self ):
        """Test case A. Tests creation of empty UserManager, creation of new UserProfiles, and access with checkPassword"""
        testManager = UserManager()

        blockListA = BlockedList()
        assert testManager.newUserProfile( "usernameA", "passwordA", blockListA ) == True, "newUserProfile not correctly determining if username is taken"

        blockListB = BlockedList()
        assert testManager.newUserProfile( "usernameA", "passwordB", blockListB ) == False, "newUserProfile not correctly determining if username is taken"

        assert testManager.newUserProfile( "usernameB", "passwordB", blockListB ) == True, "newUserProfile not correctly determining if username is taken"

        assert testManager.checkPassword( "usernameA", "passwordA" ) == blockListA, "checkPassword not returning BlockList when username + password are valid"

        assert testManager.checkPassword( "usernameB", "passwordB" ) == blockListB, "checkPassword not returning BlockList when username + password are valid"

        assert testManager.checkPassword( "usernameA", "passwordB" ) == None, "checkPassword not returning none when username + password are invalid"

# run all tests
if __name__ == "__main__":
    unittest.main()
