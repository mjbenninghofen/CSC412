from Cipher import cipher
from Attacks import tools

def main():
    # Attack on Affine cipher
    plaintext = "itwasthebestoftimesitwastheworstoftimes"
    ciphertext = cipher.affineEncrypt(23, 24, plaintext)
    
    print(plaintext, "->", ciphertext)

    tools.frequencyAnalysis(ciphertext)

if __name__ == "__main__":
    main()