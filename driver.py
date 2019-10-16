from CrypMath import crypto

def main():
    # Test basic gcd
    print("gcd(7, 11)")
    print(crypto.gcd(7, 11), end="\n\n")

    print("gcd(12, 66)")
    print(crypto.gcd(12, 66), end="\n\n")

    print("gcd(24, 4)")
    print(crypto.gcd(24, 4), end="\n\n")

    # Print all relative primes to n
    user = int(input("All relative primes up to: "))
    for i in range(1, user-1):
        if crypto.gcd(i, user) == 1:
            print(i)

if __name__ == "__main__":
    main()