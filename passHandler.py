import MD5Encryptor

# I need to wait until I can see the User files to handle interactions
# with the rest of the program
class PassHandler():

    def __init__(self, password):
        self.password = password
        self.encryptor = MD5Encryptor(self.password)
        self.hash = None

    def saveToFile(self):
        pass

    def encryptPass(self):
        md5 = self.encryptor.md5Hash()
        hex_hash = self.encryptor.hashToHex(md5)
        self.hash = hex_hash
        print(self.hash)
        
