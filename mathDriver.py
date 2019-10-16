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

    # Print all relative primes to n
    user = int(input("All relative primes up to: "))
    for i in range(1, user-1):
        if basic.gcd(i, user) == 1:
            print(i)

    # Test basic Extended Euclids
    print("Extended Euclid's (5, 17)")
    bezoutA, bezoutB, gcd, q1, q2 = basic.extendedEuclids(5, 17)

    print("Bezout coefficients:", bezoutA, bezoutB)
    print("GCD:", gcd)
    print("Quotients by the GCD:", q1, q2)

    # Test Chinese remainder theorem
    print("Chinese Remainder: x = 0 (mod 3)")
    print("                   x = 3 (mod 4)")
    print("                   x = 4 (mod 5)")
    print(chineseRemainder.chineseRemainder([0, 3, 4], [3, 4, 5]))


if __name__ == "__main__":
    main()