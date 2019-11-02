from CrypMath import basic
import string, random

def affineEncrypt(a, b, plaintext):
    plaintext = plaintext.lower()    
    ciphertext = ""

    for p in plaintext:
        if p == ' ':
            ciphertext += ' '
        else:
            p = ord(p) - 97
            c = ((a * p) + b) % 26
            ciphertext += chr(c + 97)
    
    return ciphertext

def affineDecrypt(a, b, ciphertext):
    ciphertext = ciphertext.lower()
    decrypted = ""

    inverse, _, _, _, _ = basic.extendedEuclids(a, 26)

    if inverse < 0:
        inverse += 26

    for c in ciphertext:
        if c == ' ':
            decrypted += ' '
        else:
            c = ord(c) - 97
            p = inverse * (c - b) % 26
            decrypted += chr(p + 97)

    return decrypted

def vignereEncrypt(plaintext, key):
    plaintext = plaintext.lower()
    index = 0
    ciphertext = ""
    for p in plaintext:
        p = ord( p ) - 97
        k = ord( key[index % len( key )] ) - 97

        ciphertext += chr( ( ( p + k ) % 26 ) + 97 )
        index += 1
    
    return ciphertext

def vignereDecrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    index = 0
    plaintext = ""

    for c in ciphertext:
        c = ord( c ) - 97
        k = ord( key[index % len( key )] ) - 97

        plaintext += chr( ( ( c - k ) % 26 ) + 97 )
        index += 1

    return plaintext

class ADFGX:
    header = ['A', 'D', 'F', 'G', 'X']
    alphaMatrix = []
    key = ""
    matSize = 0
    def __init__(self, key):
        self.key = key
        self.matSize = len(key)
        alphabet = list(string.ascii_lowercase)
        alphabet.remove("j")
        # Randomize the alphabet so that we can just pop elements from it
        random.shuffle(alphabet)

        # Set up the "matrix"
        for _ in range(25):
            self.alphaMatrix.append(list(alphabet.pop()))

    def __str__(self):
        out = ""

        for i in range(1, 26):
            out += str(self.alphaMatrix[i - 1]) + " "
            if i % 5 == 0:
                out += "\n"
        out += "\nKey: " + self.key

        return out

    def encrypt(self, plaintext):
        ciphertext = ""
        for p in plaintext:
            # find the character in the matrix
            for i, a in enumerate(self.alphaMatrix):
                if a[0] == p:
                    # insert the correct code into the ciphertext
                    ciphertext += self.header[i // 5]
                    ciphertext += self.header[i % 5]
            print(ciphertext)

        # extend the key to be as long as the plaintext
        while len(plaintext) > len(self.key):
            self.key += self.key

        if len(self.key) > len(plaintext):
            self.key = self.key[:(len(plaintext) - len(self.key))]

        print(self.key)

        # sort the key and move the ciphertext with it
        self.key = list(self.key)
        ciphertext = list(ciphertext)

        i = 0
        while i < len(self.key):
            if i > 0 and self.key[i] < self.key[i-1]:
                j = i
                while j >= 0 and self.key[j] < self.key[j-1]:
                    temp = self.key[j-1]
                    self.key[j-1] = self.key[j]
                    self.key[j] = temp

                    temp = ciphertext[j-2]
                    ciphertext[j-2] = ciphertext[j]
                    ciphertext[j] = temp

                    temp = ciphertext[j-1]
                    ciphertext[j-1] = ciphertext[j+1]
                    ciphertext[j+1] = temp
                    j -= 1

            elif i < len(self.key) - 1 and self.key[i] > self.key[i+1]:
                j = i
                while j < len(self.key) and self.key[i] > self.key[i+1]:
                    temp = self.key[j+1]
                    self.key[j+1] = self.key[j]
                    self.key[j] = temp
                    
                    temp = ciphertext[j+3]
                    ciphertext[j+3] = ciphertext[j+1]
                    ciphertext[j+1] = temp

                    temp = ciphertext[j+2]
                    ciphertext[j+2] = ciphertext[j]
                    ciphertext[j] = temp
                    j += 1

            print("".join(self.key), "".join(ciphertext))
            i += 1

        return "".join(ciphertext)
