'''
Testing file for the math module.
'''

from CrypMath import basic
from CrypMath import chineseRemainder

def main():
    # Test basic gcd
    print("gcd(7, 11)")
    print(basic.gcd(7, 11), end="\n\n")

    print("gcd(12, 66)")
    print(basic.gcd(12, 66), end="\n\n")

    print("gcd(24, 4)")
    print(basic.gcd(24, 4), end="\n\n")

    print(basic.gcd(13, 26))

    # Print all relative primes to n
    user = int(input("All relative primes up to: "))
    for i in range(1, user-1):
        if basic.gcd(i, user) == 1:
            print(i)

    # Test basic Extended Euclids
    print("\nExtended Euclid's (5, 17)")
    bezoutA, bezoutB, gcd, q1, q2 = basic.extendedEuclids(5, 17)

    print("Bezout coefficients:", bezoutA, bezoutB)
    print("GCD:", gcd)
    print("Quotients by the GCD:", q1, q2)

    # Test Chinese remainder theorem
    print("\nChinese Remainder: x = 1 (mod 3)")
    print("                   x = 1 (mod 4)")
    print("                   x = 1 (mod 5)")
    print("                   x = 0 (mod 7)\n")

    print(chineseRemainder.chineseRemainder([1, 1, 1, 0], [3, 4, 5, 7], doPrint = 1))

    # Test findModInverse(a, n)
    print("\nModular inverse of 4 mod 13")

    print(basic.modInverse(4, 11))

    # Test prime factorization(n)
    print("\nPrime factors of 17")

    print(basic.primeFactorization(17))

    print("\nPrime factors of 16")

    print(basic.primeFactorization(16))

    print("\nPrime factors of 15")

    print(basic.primeFactorization(15))

    # Test isPrimativeRoot(a, n)
    print("\nIs 6 a primitive root mod 131?")

    print(basic.isPrimitiveRoot(6, 131, doPrint=True))

    print("\nHow about 15?")

    print(basic.isPrimitiveRoot(15, 131, doPrint=True))


if __name__ == "__main__":
    main()