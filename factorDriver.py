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

if __name__ == "__main__":
    main()