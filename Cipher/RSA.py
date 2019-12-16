from CrypMath import basic
import random

'''
makeKeys is the heart of this RSA implementation. It creates both the public
and private keys based on two primes q and p. First, n and phi are calculated.
Then a random prime between 1 and phi is generated and the multiplicative
inverse of that prime mod phi is calculated using the extendedEuclidean
algorithm. The public key is packaged up as a tuple containing e and n, and
the private key with d and n. This is slow at the moment because of the call
to getAllPrimes. phi is a very large number when and realistic values for p
and q are used, so getting all the primes up to phi is verry inefficient.
'''
def makeKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    primes = basic.getAllPrimes(phi - 1)
    e = primes[random.randint(0, len(primes))]

    d, _, _, _, _ = basic.extendedEuclids(e, phi)

    return ((e, n), (d, n))

'''
makeKeysFast is an improvement on my naive first approach in which all the
primes less than phi were calculated. Instead of that, a random value less
that phi is created and tested to be prime, this is repeated until a prime
is found. makeKeys took about 10 seconds using the testing values in
cipherDriver.py, this takes less than half a second on my machine.
'''
def makeKeysFast(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)

    while not basic.isPrime(e, 10):
        e = random.randint(2, phi - 1)

    d, _, _, _, _ = basic.extendedEuclids(e, phi)

    return ((e, n), (d, n))

'''
encrypt uses the package pk containing e and n to encrypt. First the key and n
are extracted from the tuple, then for each character in the plaintext it is
converted to an integer and taken to the power key mod n. That is appended to
the ciphertext array and when all characters have been processed the ciphertext
array is returned.
'''
def encrypt(pk, plaintext):
    key, n = pk

    ciphertext = []

    for p in plaintext:
        ciphertext.append(pow(ord(p), key, n))

    return ciphertext

'''
decrypt works the same way as encrypting but the values are converted to
characters and appended to a string instead.
'''
def decrypt(pk, ciphertext):
    key, n = pk

    plaintext = ""

    for c in ciphertext:
        plaintext += chr(pow(c, key, n))

    return plaintext