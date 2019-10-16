def gcd(a, b):
    while a != b and b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def extendedEuclids( a, b ):
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