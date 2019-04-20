import unittest
from AesManager import *



class SimpleTestCase( unittest.TestCase ):

    def testA( self ):
        """Test case A submit a password and check if password encrypts and decrypts properly"""
        testManager = AesManager()
        passwordA = "passwordA"
        enc = testManager.encrypt(passwordA)
        assert enc != passwordA

        
        dec = testManager.decrypt(enc)
        assert dec.decode("utf-8") == passwordA
        
        """Test case B decrypt an already encrypted password"""
        testManager = AesManager()
        passwordB = "passwordB"
        enc = testManager.encrypt(passwordB)
        key = testManager.key
        nonce = testManager.nonce

        testManager = AesManager(key, nonce)
        dec = testManager.decrypt(enc)
        assert dec.decode("utf-8") == passwordB



# run all tests
if __name__ == "__main__":
    unittest.main()
