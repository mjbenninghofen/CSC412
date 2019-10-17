from Cipher import cipher
from Attacks import tools

def main():
    # Affine Cipher
    a = int(input("Affine Cipher\nEnter a: "))
    b = int(input("Enter b: "))
    plaintext = input("Enter plaintext: ")

    ciphertext = cipher.affineEncrypt(a, b, plaintext)
    print("Encrypting:", plaintext, "->", ciphertext)

    plaintext = cipher.affineDecrypt(a, b, ciphertext)
    print("Decrypting:", ciphertext, "->", plaintext)

    # Vignere Cipher
    plaintext = input("\nVignere Cipher\nEnter plaintext: ")
    key = input("Enter key: ")

    ciphertext = cipher.vignereEncrypt(plaintext, key)
    print("Encrypting:", plaintext, "->", ciphertext)

    print("\nDoing frequency analysis on", ciphertext)
    tools.frequencyAnalysis(ciphertext)

    plaintext = cipher.vignereDecrypt(ciphertext, key)
    print("\nDecrypting:", ciphertext, "->", plaintext)

    ADFGX = cipher.ADFGX("testKey")

    print("\n" + ADFGX)

if __name__ == "__main__":
    main()