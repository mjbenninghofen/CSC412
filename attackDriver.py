'''
Testing file for the attacks module.
'''

from Cipher import cipher
from Attacks import tools, classicAttacks, detectEnglish


def main():
    # Attack on Affine cipher
    print("Affine Cipher Attack:\n")
    plaintext = "it was the best of times it was the worst of times"
    ciphertext = cipher.affineEncrypt(23, 24, plaintext)

    print(plaintext, "->", ciphertext)

    plaintext = classicAttacks.affine(ciphertext)

    print(ciphertext, "->", plaintext)
    # Attack on Vigenere cipher
    print("\nVigenere Cipher Attack:\n")
    plaintext = "this is a string of text that is english it wont work with other languages"
    key = "stringkey"
    ciphertext = cipher.vigenereEncrypt(plaintext, key)

    extractedPlaintext, acquiredKey = classicAttacks.vigenere(ciphertext)

if __name__ == "__main__":
    main()