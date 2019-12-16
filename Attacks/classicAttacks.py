import string, itertools
from Attacks import tools, detectEnglish
from Cipher import cipher

# This is really bad, but it's what I could figure out on my own. There
# is a better version in break_affine_2.py but it is not mine.
def affine(ciphertext, wordLength=15):
    # Try all 312 options looking for english
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for j in range(0, 25):
            plaintextAttempt = cipher.affineDecrypt(i, j, ciphertext)

            for k in range(3, wordLength):
                if detectEnglish.isEnglish(plaintextAttempt[:k]):
                    print("Is this correct?")
                    print(plaintextAttempt)

                    user = input("(y/N)")

                    if user.lower() == 'y':
                        print("a =", i, "b =", j)
                        return plaintextAttempt
                    break

def vigenere(ciphertext):
    alphabet = string.ascii_lowercase
    keyLength = tools.keyLength(ciphertext, 15, doPrint=False)
    print("Keylength:", keyLength)

    # Generate all possible strings of length keyLength and test
    for char in itertools.product(alphabet, repeat=keyLength):
        keyAttempt = "".join(char)
        plainAttempt = cipher.vigenereDecrypt(ciphertext, keyAttempt)

        # If we can detect English in the output, print it and check with user
        if detectEnglish.isEnglish(plainAttempt):
            print(plainAttempt)
            answer = input("Is this right? (y/N)").lower()

            if answer == 'y':
                print("Key:", keyAttempt)
                return plainAttempt, keyAttempt
