from CrypMath import basic
import random

def makeKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    primes = basic.getAllPrimes(phi - 1)
    e = primes[random.randint(0, len(primes))]

    d, _, _, _, _ = basic.extendedEuclids(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk

    ciphertext = []

    for p in plaintext:
        ciphertext.append((ord(p) ** key) % n)

    return ciphertext

def decrypt(pk, ciphertext):
    key, n = pk

    plaintext = ""

    for c in ciphertext:
        plaintext += chr((c ** key) % n)

    return plaintext