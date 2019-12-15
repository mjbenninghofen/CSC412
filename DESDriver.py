from Cipher import simpleDES
import bitstring

def main():
    '''
    Simple DES, doing this in Python was a mistake. Something is wrong
    somewhere, and I need to move on to the other parts of the project
    before I run completely out of time.
    '''
    print("\nSimple DES:")

    key = bitstring.BitArray('0b101010101')
    plaintext = bitstring.BitArray('0b111000001110')

    print("Encrypting: [", plaintext, "] with key: [", key.bin, "]")

    ciphertext = simpleDES.encrypt(key, plaintext)

    print("Decrypting: [", ciphertext, "] with key: [", key.bin, "]")

    plaintext = simpleDES.decrypt(key, ciphertext)

    print("Decrypted Message:", plaintext)

if __name__ == "__main__":
    main()