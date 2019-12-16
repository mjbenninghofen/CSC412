from CrypMath import basic

'''
There are certain things whose number is unknown. If we count them by threes,
we have two left over; by fives, we have three left over; and by sevens, two
are left over. How many things are there?

Originally this question was posed by Sunzi, a Chinese mathematician  in the
3rd century.

This function answers that question.
'''
def chineseRemainder(n, a, doPrint=0):
    prod = 1
    x = 0

    for i in range(len(a)):
        if a[i] > 0:
            prod *= a[i]
    
    for i in range(len(a)):
        m = prod // a[i]

        if doPrint == 1:
            print("x =", n[i], "( mod", a[i], "), M =", m, end=', ')
        
        value = 1
        while (value * m) % a[i] != 1:
            value += 1
        
        x += n[i] * m * value
        
        if doPrint == 1:
            print("y = ", value, ", product total = ", x, sep='')

    if doPrint == 1:
        print(x, "-", prod, "=", x - prod)

    return x - prod
