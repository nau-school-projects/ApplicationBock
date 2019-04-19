from Crypto.Cipher import AES
from Crypto import Random
from random import randint

class AesManager():

    def __init__( self, key=None, nonce=None ):
        if( key == None ):
           key = Random.get_random_bytes(16)
        self.key = key
        self.aes = AES.new(key, AES.MODE_EAX )
        if( nonce == None ):
            self.nonce = self.aes.nonce
        self.nonce = nonce

    def encrypt(self, password):
        password = password.encode('utf-8')
        encrypted = self.aes.encrypt(password)
        return encrypted

    def decrypt(self, encrypted):
        self.aes = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce)
        decrypted = self.aes.decrypt(encrypted)
        return decrypted
        
    
