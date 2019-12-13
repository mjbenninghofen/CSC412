import math
from CrypMath import basic

def factor(n, m=0, b=5):
    # Fermat's factorization method
    if m == 0:
        a = math.ceil(math.sqrt(n))

        b_sq = (a ** 2) - n

        while not isSquare(b_sq):
            a += 1
            b_sq = b_sq + 2*a + 1

        return a - math.sqrt(b_sq)

    # Pollard's rho
    if m == 1:
        x = 2
        y = 2
        d = 1

        def g(x):
            return ((x ** 2) + 1) % n

        while d == 1:
            x = g(x)
            y = g(g(y))
            d = basic.gcd(abs(x - y), n)

        if d == n:
            return None

        return d

    # Pollard's P-1
    if m == 2:
        c = 2
        for p in basic.getAllPrimes(b):
            pp = p
            while pp < b:
                c = pow(c, p, n)
                pp = pp * p
        g = basic.gcd(c-1, n)
        if 1 < g < n:
            return g

        return None


def isSquare(n):
    return math.sqrt(n) - math.floor(math.sqrt(n)) == 0
