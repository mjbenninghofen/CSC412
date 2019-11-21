from Attacks import detectEnglish
from Cipher import cipher
from CrypMath import basic

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
    #keyLength = tools.keyLength(ciphertext, 20)
    pass