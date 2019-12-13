import bitstring

def encrypt(key, plaintext):
    plain_bs = bitstring.BitArray()
    cipher_bs = bitstring.BitArray()

    K = key[:8]

    for p in plaintext:
        plain_bs.append(bin(ord(p)))

    while not len(plain_bs) % 12 == 0:
        plain_bs.append(bitstring.BitArray('0b0'))

    print(plain_bs.bin)

    for i in range((len(plaintext) * 8) // 12):
        L = plain_bs[(i * 12): (i * 12) + 6]
        R = plain_bs[(i * 12) + 6: (i * 12) + 12]

        for _ in range(4):
            temp = bitstring.BitArray(R)

            R = f(R, K) ^ L

            L = temp

        cipher_bs.append(L)
        cipher_bs.append(R)

    return cipher_bs

def decrypt(key, cipher_bs):
    plain_bs = bitstring.BitArray()
    plaintext = ""

    K = key[8:]
    K.append(key[:7])

    while not len(cipher_bs) % 12 == 0:
        cipher_bs.append(bitstring.BitArray('0b0'))

    for i in range(len(cipher_bs) // 12):
        L = cipher_bs[(i * 12): (i * 12) + 6]
        R = cipher_bs[(i * 12) + 6: (i * 12) + 12]

        for _ in range(4):
            temp = R

            R = f(R, K) ^ L

            L = temp

        plain_bs.append(L)
        plain_bs.append(R)

    for i in range(len(plain_bs) // 8):
        val = plain_bs[i * 8: (i * 8) + 8].int
        if (val > 0):
            plaintext += chr(val)
        else:
            plaintext += "-"

    return plaintext
        

def f(R, K):
    R = expand(R)
    R = R ^ K

    L = R[:4]
    R = R[4:]

    L = S1[L.tobytes()]
    R = S2[R.tobytes()]

    final = bitstring.BitArray(0)
    final.append(L)
    final.append(R)

    return final

def expand(short):
    expanded = bitstring.BitArray(8)

    expanded.set(short[0], 0)
    expanded.set(short[1], 1)
    expanded.set(short[3], 2)
    expanded.set(short[2], 3)
    expanded.set(short[3], 4)
    expanded.set(short[2], 5)
    expanded.set(short[4], 6)
    expanded.set(short[5], 7)

    return expanded

S1 = {
    b'\x00': bitstring.BitArray('0b101'), b'\x10': bitstring.BitArray('0b010'),
    b'\x20': bitstring.BitArray('0b001'), b'\x30': bitstring.BitArray('0b110'),
    b'\x40': bitstring.BitArray('0b011'), b'\x50': bitstring.BitArray('0b100'),
    b'\x60': bitstring.BitArray('0b111'), b'\x70': bitstring.BitArray('0b000'),
    b'\x80': bitstring.BitArray('0b001'), b'\x90': bitstring.BitArray('0b100'),
    b'\xa0': bitstring.BitArray('0b110'), b'\xb0': bitstring.BitArray('0b010'),
    b'\xc0': bitstring.BitArray('0b000'), b'\xd0': bitstring.BitArray('0b111'),
    b'\xe0': bitstring.BitArray('0b101'), b'\xf0': bitstring.BitArray('0b011')
}

S2 = {
    b'\x00': bitstring.BitArray('0b100'), b'\x10': bitstring.BitArray('0b000'),
    b'\x20': bitstring.BitArray('0b110'), b'\x30': bitstring.BitArray('0b101'),
    b'\x40': bitstring.BitArray('0b111'), b'\x50': bitstring.BitArray('0b001'),
    b'\x60': bitstring.BitArray('0b011'), b'\x70': bitstring.BitArray('0b010'),
    b'\x80': bitstring.BitArray('0b101'), b'\x90': bitstring.BitArray('0b011'),
    b'\xa0': bitstring.BitArray('0b000'), b'\xb0': bitstring.BitArray('0b111'),
    b'\xc0': bitstring.BitArray('0b110'), b'\xd0': bitstring.BitArray('0b010'),
    b'\xe0': bitstring.BitArray('0b001'), b'\xf0': bitstring.BitArray('0b100')
}