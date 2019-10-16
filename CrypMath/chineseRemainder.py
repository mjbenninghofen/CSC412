from CrypMath import basic

def chineseRemainder(n, a):
    bigN = 1
    answer = 0

    for i in range(0, len(n)):
        if n[i] != 0:
            bigN *= n[i]

    for i in range(len(n)):
        if n[i] == 0:
            p = 0
        else:
            p = bigN // n[i]
        inverse, _, _, _, _ = basic.extendedEuclids( p, n[i] )
        answer += a[i] * inverse * p

    return (answer % bigN)
