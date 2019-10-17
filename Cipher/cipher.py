from CrypMath import basic
import string, random

def affineEncrypt(a, b, plaintext):
    plaintext = plaintext.lower()    
    ciphertext = ""

    for p in plaintext:
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

    def setMatrix(self, inMatrix):
        pass
