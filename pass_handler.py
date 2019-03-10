import MD5_Encryptor

# I need to wait until I can see the User files to handle interactions
# with the rest of the program
class Pass_Handler():

    def __init__(self, password):
        self.password = password
        self.encryptor = MD5_Encryptor(self.password)
        self.hash = None

    def save_to_file(self):
        pass

    def encrypt_pass(self):
        md5 = self.encryptor.md5_hash()
        hex_hash = self.encryptor.hash_to_hex(md5)
        self.hash = hex_hash
        print(self.hash)
        
