from math import sqrt
import random

# gcd(a, b) is used to find the greatest common denominator
# between a and b. If the gcd of 2 values is 1 we call them
# relatively prime. A prime number has gcd 1 with all integers.
def gcd(a, b):
    while a != b and b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# This extended Euclidean algorithm is based on the pseudocode
# section of this wikipedia page:
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# It returns the Bezout coefficients, the GCD, and the
# quotients by the GCD. It just so happens that the first
# Bezout coefficient is the inverse of a (mod b) because
# the Bezout coefficients are x and y from:
#     ax + by = gcd(a, b)
# I take advantage of that in my affine decrypt function.
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

# modInverse finds the multiplicative inverse of a (mod n)
# in a more efficent way that the Extended Euclidean algorithm
# above. 
def modInverse(a, n):
    if gcd(a, n) != 1:
        return -1

    for i in range(n):
        if ((a * i) % n) == 1:
            return i
    return -1

# primeFactorization returns a list of prime factors for the
# given input. It does this in a similarly to how I do it on
# paper, first by dividing by 2 until it is odd, then going
# up the integers starting at 3 until some value is found
# that will divide the remaining value evenly. There may be
# a more efficient way to do this, as the only optimization
# that I made was to only go up to sqrt(n) + 1 while searching
# for factors.
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

# Fermat's totient or phi(n) is the number of positive integers less
# than n which are relatively prime to n. I use it in my isPrimitiveRoot
# function, but it can be used for lots of things.
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

# isPrime is based off Fermat's factoring algorithm, it uses Fermat's
# little theorem, a^(p-1) is congruent to 1 (mod p) to determine if n
# is probably prime or not. k is the number of random values to test
# against, where they will be x in this equation:
#     x^(n-1) % n = 1
# If that is true, then n is probably prime, however, that will be
# repeated with k different values between 1 and n-1 to be more
# confident in the answer. I have done it this way so that later,
# when none of my code works, I can blame it on this. Good Luck!
def isPrime(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        x = random.randint(1, n-1)

        if pow(x, n-1, n) != 1: # power function with mod included! Nice!
            return False
    
    return True

# randomPrime finds a random prime between 2^(b)-1 and 2^(b+1)-1.
# These bounds are guaranteed to be odd, so we can iterate through
# the values by two to skip all the even numbers. To ensure that
# the returned value is not just the first prime that is encountered,
# a list of all primes between the bounds is formed and then chosen
# from randomly.
def randomPrime(b):
    upperBound = pow(2, b + 1) - 1
    lowerBound = pow(2, b) - 1

    primes = []

    for i in range(upperBound - lowerBound, step=2):
        if isPrime(i, 10):
            primes.append(i)

    return primes[random.randint(0, len(primes))]

# getAllPriems is the same algorithm from above, but it returns a
# list of all positive primes less than b.
def getAllPrimes(b):
    primes = [2]

    for i in range(3, b, 2):
        if isPrime(i, 10):
            primes.append(i)

    return primes

# isPrimitiveRoot determines if a is a primitive root of n. There is
# an optional argument to print an outline of the algorithm as it goes.
# First, phi(n) is calculated and the prime factorization of that value
# is found.
# Next, a^(p) % n where p is phi(n) / a prime factor of phi(n) for each
# unique prime factor.
# Finally, if a^(p) % n is equal to 1 we know that a is not a primitive
# root (mod n). If, on the other hand, none of the unique prime factors
# result in this outcome, a is a primitive root (mod n).
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