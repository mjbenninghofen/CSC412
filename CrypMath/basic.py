from math import sqrt

def gcd(a, b):
    while a != b and b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def extendedEuclids(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        
        temp = r
        r = old_r - quotient * temp
        old_r = temp

        temp = s
        s = old_s - quotient * temp
        old_s = temp

        temp = t
        t = old_t - quotient * temp
        old_t = temp    

    #print("Bezout coefficients:", old_s, old_t)
    #print("GCD:", old_r)
    #print("Quotients by the GCD:", t, s)

    return old_s, old_t, old_r, t, s

def modInverse(a, n):
    if gcd(a, n) != 1:
        return -1

    for i in range(n):
        if ((a * i) % n) == 1:
            return i
    return -1

def primeFactorization(n):
    primeFactors = []

    while n % 2 == 0:
        primeFactors.append(2)
        n /= 2
    
    for i in range(3, int(sqrt(n))+1):
        while n % i == 0:
            primeFactors.append(i)
            n /= i

    if n > 2:
        primeFactors.append(int(n))

    return primeFactors

def fermatTotient(n):
    result = n

    p = 2
    while p ** 2 <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p += 1

    if n > 1:
        result = result * (1.0 - (1.0 / float(n)))

    return int(result)

def isPrimitiveRoot(a, n, doPrint = False):
    s = fermatTotient(n)
    if doPrint:
        print("phi(", n, ") =", s)
    
    primeFactors = primeFactorization(s)
    if doPrint:
        print("prime factors of", s, ":", primeFactors)

    powers = []

    for p in primeFactors:
        if not powers.__contains__(s/p):
            powers.append(int(s/p))

    if doPrint:
        print("powers to test:", powers)

    for p in powers:
        if doPrint:
            print(a, "**", p, "%", n, "=", (a ** p) % n)
        if (a ** p) % n == 1:
            return False
    
    return True