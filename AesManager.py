from Crypto.Cipher import AES
from Crypto import Random
from random import randint

class AesManager():

    def __init__( self, key=None, nonce=None ):
        
        if( key == None ):
            print( "generated new key" )
            self.key = Random.get_random_bytes(16)
        else:
            self.key = key
            
        self.aes = AES.new(self.key, AES.MODE_EAX )
        
        if( nonce == None ):
            print( "generated new nonce" )
            self.nonce = self.aes.nonce
        else:
            self.nonce = nonce

        if( self.nonce == None or self.key == None ):
            print( "done goofed" )
        

    def encrypt(self, password):
        password = password.encode('utf-8')
        encrypted = self.aes.encrypt(password)
        return encrypted

    def decrypt(self, encrypted):
        self.aes = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce)
        decrypted = self.aes.decrypt( encrypted.encode('utf-8') )
        return decrypted
        
    
