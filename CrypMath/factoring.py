import math
from CrypMath import basic

def factor(n, m=0, b=5):
    # Fermat's factorization method:
    if m == 0:
        a = int(math.ceil(math.sqrt(n)))

        b_sq = (a ** 2) - n

        while not isSquare(b_sq):
            a += 1
            b_sq = (a ** 2) - n
            b = int(math.sqrt(b_sq))

        p = a+b
        q = a-b

        assert n == p * q

        return p, q

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

        return d, n // d

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
            return g, n // g

        return None

'''
Shank's square forms factorization is an improvement on Fermat's Factorization
method. It is not the most efficient method, but it is small enough to fit on
modest calculators. This implementation is based on the algorithm section of 
this page: https://en.wikipedia.org/wiki/Shanks%27s_square_forms_factorization
'''
def SQUFOF(n, k, doPrint=False):
    P = [math.floor(math.sqrt(k * n))]
    Q = [1, (k * n) - (P[0] ** 2)]
    b = [None, math.floor((P[0] * 2) / Q[1])]

    if doPrint: print("i:", 0, P[0], Q[0], b[0])

    i = 1
    while not (isSquare(Q[i]) and i % 2 == 0):
        b.append((P[0] + P[i-1]) // Q[i])
        P.append(b[i + 1] * Q[i] - P[i-1])
        Q.append(Q[i-1] + b[i+1] * (P[i-1] - P[i]))

        if doPrint: print("i:", i, P[i], Q[i], b[i+1])

        i += 1
    
    if doPrint: print("i:", i, "--", Q[i], "-\n")

    tempQ = Q[i]
    tempP = P[i-1]
    P0 = P[0]

    Q.clear()
    P.clear()
    b.clear()

    b.append(int((P0 - tempP) // math.sqrt(tempQ)))
    P.append(int(b[0] * math.sqrt(tempQ) + tempP))
    Q.append(int(math.sqrt(tempQ)))
    Q.append(((k * n) - (P[0] ** 2)) // Q[0])

    if doPrint: print("i:", 0, P[0], Q[0], b[0])

    i = 1
    while True:
        b.append((P[0] + P[i-1]) // Q[i])
        P.append(b[i] * Q[i] - P[i-1])
        Q.append(Q[i-1] + b[i] * (P[i-1] - P[i]))

        if doPrint: print("i:", i, P[i], Q[i], b[i])

        if P[i] == P[i-1]:
            break

        i += 1

    factor = basic.gcd(n, P[i])

    if doPrint: print("gcd(", n, ",", P[i], ") =", factor, "\n")

    return (factor, n // factor)

def isSquare(n):
    return math.sqrt(n) - math.floor(math.sqrt(n)) == 0
