import sys

def main(argv):
    print("Assuming pairwise coprime positive integers as input.")

    if len(argv) % 2 != 1:
        print("Uneven number of inputs")
        sys.exit()

    n = list()
    a = list()
    bigN = 1
    answer = 0

    for i in range( 1, len( argv ) - 1, 2):
        bigN *= int( argv[i] )
        n.append( int( argv[i] ) )
        a.append( int( argv[i+1] ) )
        #print(bigN, argv[i], argv[i+1])


    for i in range( len( n ) ):
        p = bigN // n[i]
        inverse, _, _, _, _ = extendedEuclids( p, n[i] )
        answer += a[i] * inverse * p

    print( answer % bigN)

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

if __name__ == "__main__":
    main(sys.argv)
