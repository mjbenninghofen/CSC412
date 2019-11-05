from Cipher import cipher
from Attacks import tools, classicAttacks, detectEnglish


def main():
    # Attack on Affine cipher
    print("Affine Cipher Attack:\n")
    plaintext = "it was the best of times it was the worst of times"
    ciphertext = cipher.affineEncrypt(23, 24, plaintext)
    
    print(plaintext, "->", ciphertext)

    # Attack on Vigenere cipher
    print("\nVigenere Cipher Attack:\n")
    plaintext = "this is a string of text that is english it wont work with other languages"
    key = "stringkey"
    ciphertext = cipher.vignereEncrypt(plaintext, key)

    extractedPlaintext, acquiredKey = classicAttacks.vigenere(ciphertext)

if __name__ == "__main__":
    main()