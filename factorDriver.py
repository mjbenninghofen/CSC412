'''
Testing file for the factoring code.
'''

from CrypMath import factoring

def main():
    testValue = 4421 * 2785
    print("Factoring", testValue)

    print("Fermat's Factoring Algorithm:")
    factors = factoring.factor(testValue)
    print(factors)

    print("Pollard's rho:")
    factors = factoring.factor(testValue, 1)
    print(factors)

    print("Pollard's P-1:")
    factors = factoring.factor(testValue, 2)
    print(factors)

    testValue = 5959
    print("\nFactoring", testValue)

    print("Fermat's Factoring Algorithm:")
    factors = factoring.factor(testValue)
    print(factors)

    print("Pollard's rho:")
    factors = factoring.factor(testValue, 1)
    print(factors)

    print("Pollard's P-1:")
    factors = factoring.factor(testValue, 2)
    print(factors)

    print("Shank's Square forms, n = 11111, k = 1:")
    factors = factoring.SQUFOF(11111, 1, doPrint = True)
    print("Factors of 111111:", factors)

    print("Factors of 12312921:", factoring.SQUFOF(12312921, 1))
    print("Factors of 83120312891:", factoring.SQUFOF(83120312891, 1))


if __name__ == "__main__":
    main()