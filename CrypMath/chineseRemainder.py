from CrypMath import basic

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
