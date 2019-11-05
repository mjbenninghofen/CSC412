import string, itertools
from Attacks import tools, detectEnglish
from Cipher import cipher

def affine(ciphertext):
    pass

def vigenere(ciphertext):
    alphabet = string.ascii_lowercase
    keyLength = tools.keyLength(ciphertext, 15, doPrint=True)
    print("Keylength:", keyLength)

    # Generate all possible strings of length keyLength and test
    for char in itertools.product(alphabet, repeat=keyLength):
        keyAttempt = "".join(char)
        plainAttempt = cipher.vignereDecrypt(ciphertext, keyAttempt)

        # If we can detect English in the output, print it and check with user
        if detectEnglish.isEnglish(plainAttempt):
            print(plainAttempt)
            answer = input("Is this right? (y/N)").lower()

            if answer == 'y':
                print("Key:", keyAttempt)
                return plainAttempt, keyAttempt
