from Cipher import simpleDES
import bitstring

def main():
    # Simple DES, doing this in Python was a mistake
    print("\nSimple DES:")

    key = bitstring.BitArray('0b101010101')

    ciphertext = simpleDES.encrypt(key, "plaintext")

    print("Encrypted Message:", ciphertext.bin)

    plaintext = simpleDES.decrypt(key, ciphertext)

    print("Decrypted Message:", plaintext)

if __name__ == "__main__":
    main()