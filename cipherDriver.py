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
    tools.frequencyAnalysis(ciphertext, doPrint=True)

    plaintext = cipher.vignereDecrypt(ciphertext, key)
    print("\nDecrypting:", ciphertext, "->", plaintext)

    # Blum Blum Shub
    print("\nBlum Blum Shub pseudorandom bit generation: ")
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    s = int(input("Enter seed: "))
    l = int(input("Enter desired length in bytes: "))

    randomBitString = cipher.BBS(p, q, s, l)

    print(bin(randomBitString))

    plaintext = input("\nEnter string to encrypt with this sequence: ")

    ciphertext = cipher.xor(plaintext, randomBitString)

    print(plaintext, "->", ciphertext)

    plaintext = cipher.xor(ciphertext, cipher.BBS(p, q, s, l))

    print(ciphertext, "->", plaintext)

    # ADFGX cipher
    print("\nADFGX cipher:")
    ADFGX = cipher.ADFGX(input("Enter key: "))

    print("\n" + str(ADFGX))

    plaintext = input("Enter plaintext: ")
    
    ciphertext = ADFGX.encrypt(plaintext)
    print("Encrypting:", plaintext, "->", ciphertext)

if __name__ == "__main__":
    main()