import math

class MD5_Encryptor():
    
    def __init__(self, password):
        self.rotates = [ 7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
                  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
                  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
                  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 ]
        self.constants = []
        set_constants()
        self.password = password
        self.a0 = 0x67452301
        self.b0 = 0xefcdab89
        self.c0 = 0x98badcfe
        self.d0 = 0x10325476
        self.func_A = lambda b, c, d: (b & c) | (~b & d)
        self.func_B = lambda b, c, d: (d & b) | (~d & c)
        self.func_C = lambda b, c, d: b ^ c ^ d
        self.func_D = lambda b, c, d: c ^ (b | ~d)
        

    def set_constants(self):
        for(i in range(64)):
            self.constants[i] = math.floor(2**32 * (int(abs(math.sin(i+1)))))


    def md5_hash(self):
        pass_bytes = bytearray(self.password, 'utf-8')
        pass_length = (8 * len(self.password)) % (2**64)
        pass_bytes.append(0b01)
        while( len(pass_bytes) % 512 != 448 ):
            pass_bytes.append(0)
        pass_bytes += pass_length.to_bytes(8, byteorder="little")
        words = [16]
        i = 0
        for chunk in range(0, len(pass_bytes), 32):
            words[i] = pass_bytes[chunk:chunk+32]
            i += 1
        A = self.a0
        B = self.b0
        C = self.c0
        D = self.d0
        rotator, index = 0
        for( i in range(64)):
            if( 0 <= i < 16 ):
                rotator = self.func_A(B, C, D)
                index = i
            else if( 16 <= i < 32 ):
                rotator = self.func_B(B, C, D)
                index = (5*i + 1) % 16
            else if( 32 <= i < 48 ):
                rotator = self.func_C(B, C, D)
                index = (3*i + 5) % 16
            else if( 48 <= i < 64 ):
                rotator = self.func_D(B, C, D)
                index = (7*i) % 16
            # Now rotate A, B, C, D, the rotator, and the index
            rotator = rotator + A + self.constants[i] + int.from_bytes(words[index], byteorder="little")
            A = D
            D = C
            C = B
            B = B + rotate_left(rotator, self.rotates[i])
        a0 += A
        b0 += B
        c0 += C
        d0 += D
        digest = [a0, b0, c0, d0]
        md5Hash = 0
        for( i in range(4) ):
            md5Hash += (digest[i] << (32 * i))
        return md5Hash

    def hash_to_hex(self, message):
        raw = message.to_bytes(16, byteorder="little")
        return '{:032x}'.format(int.from_bytes(raw, byteorder="big"))


    def rotate_left(self, value, ammount):
        return ((value << ammount) | (x >> (32 - ammount)))
    
        

