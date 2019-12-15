from Cipher import cipher, RSA
from Attacks import tools

def main():
    a = 15
    b = 17
    plaintext = "thisissometext"

    ciphertext = cipher.affineEncrypt(a, b, plaintext)
    print("Affine Cipher:\nEncrypting: [", plaintext, "], a = ", a, ", b = ", b)
    print("Ciphertext:", ciphertext)

    plaintext = cipher.affineDecrypt(a, b, ciphertext)
    print("Decrypting:", ciphertext, "->", plaintext)

    # Vigenere Cipher
    plaintext = "itwasthebestoftimesitwastheworstoftimes"
    key = "caesar"

    ciphertext = cipher.vigenereEncrypt(plaintext, key)
    print("\nVigenere Cipher:\nEncrypting: [", plaintext, "], key = [", key, "]")
    print("Ciphertext:", ciphertext)

    print("\nDoing frequency analysis on [", ciphertext, "]")
    tools.frequencyAnalysis(ciphertext, doPrint=True)

    plaintext = cipher.vigenereDecrypt(ciphertext, key)
    print("\nDecrypting:", ciphertext, "->", plaintext)

    # Blum Blum Shub
    print("\nBlum Blum Shub pseudorandom bit generation: ")
    p = 883
    q = 977
    s = 5
    l = 5
    plaintext = "texts"

    print("p = ", p, "q = ", q, "seed = ", s, "length in bytes = ", l)

    randomBitString = cipher.BBS(p, q, s, l)

    print(bin(randomBitString))

    print("Encrypting: [", plaintext, "] using this bitstring")

    ciphertext = cipher.xor(plaintext, randomBitString)
    print("Ciphertext: [", ciphertext, "]")

    print("Decrypting: [", ciphertext, "]")
    
    plaintext = cipher.xor(ciphertext, cipher.BBS(p, q, s, l))
    print("Plaintext: [", plaintext, "]")

    # ADFGX cipher
    print("\nADFGX cipher:")
    key = "churchill"
    ADFGX = cipher.ADFGX(key)

    print(str(ADFGX))

    plaintext = input("Enter plaintext: ")
    
    ciphertext = ADFGX.encrypt(plaintext)
    print("Encrypting:", plaintext, "->", ciphertext)

    # RSA cipher
    print("\nRSA encryption:")
    p = 7043
    q = 911

    plaintext = "iamalmostdonewiththisproject"

    print("P =", p, "Q =", q)

    public, private = RSA.makeKeys(p, q)

    print("Public:", public, ", Private:", private)

    print("Encrypting [", plaintext, "] with private key")

    ciphertext = RSA.encrypt(private, plaintext)

    print("Ciphertext: [", ciphertext, "]")

    print("Decrypting [", ciphertext, "] with public key")

    plaintext = RSA.decrypt(public, ciphertext)

    print("Plaintext: [", plaintext, "]")

if __name__ == "__main__":
    main()