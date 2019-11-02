from Cipher import cipher
from Attacks import tools, detectEnglish


def main():
    # Attack on Affine cipher
    print("Affine Cipher Attack:\n")
    plaintext = "it was the best of times it was the worst of times"
    ciphertext = cipher.affineEncrypt(23, 24, plaintext)
    
    print(plaintext, "->", ciphertext)

    print(detectEnglish.isEnglish(plaintext))

if __name__ == "__main__":
    main()