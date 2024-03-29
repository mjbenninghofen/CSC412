import bitstring

'''
Simple DES encryption. Each block is 12 bits (which was interesting
to do in python) and the key is 9 bits. K[i] is generated by taking
bits i through 8 of the key (zero indexed) and prepending bits 0
through 8 - the length of that subkey. All the keys are generated
before using them simply to make decryption easier. For each 12 bit
block in the input bitstring L and R are created from the higher
6 bits of the block and the lower 6 bits respectively. Then four
rounds of a Fiestel system take place in which L is replaced by R
and R is replaced by f(R, K[i]) XOR'd with L. The f function
consists of expanding the input R to 8 bits and XOR'ing it with
K[i], then it is split into two halves, L and R, and those 4 bit
values are used to index into the two S-Boxes, S1 and S2. The
S-Boxes return 3 bit values which are then concatenated to form the
final output of the f function. The S-Boxes in this case are
dictionaries.
'''
def encrypt(key, plain_bs):
    cipher_bs = bitstring.BitArray()
    keys = []

    while not len(plain_bs) % 12 == 0:
        plain_bs.append(bitstring.BitArray('0b0'))

    for i in range(4):
        temp = key[i:]
        temp = temp[:8]
        temp.prepend(key[0: 8 - len(temp)])

        keys.append(temp)

    for i in range(len(plain_bs) // 12):
        L = plain_bs[(i * 12): (i * 12) + 6]
        R = plain_bs[(i * 12) + 6: (i * 12) + 12]

        for j in range(4):
            temp = bitstring.BitArray(R)

            R = f(R, keys[j]) ^ L

            L = temp

        print("E", L, R)

        cipher_bs.append(L)
        cipher_bs.append(R)

    return cipher_bs

"""
Simple DES decryption. Decryption is almost identical to
ncryption in that 4 rounds of the Fiestel system are used.
However, the keys are used in reverse order, hense using a
premade list of keys that can easily be reversed, and the
blocks are run in reverse staring at the end of the input
bitstring and going towards the beginning.
"""
def decrypt(key, cipher_bs):
    plain_bs = bitstring.BitArray()
    keys = []

    while not len(cipher_bs) % 12 == 0:
        cipher_bs.append(bitstring.BitArray('0b0'))

    for i in range(4):
        temp = key[i:]
        temp = temp[:8]
        temp.prepend(key[0: 8 - len(temp)])

        keys.append(temp)
    
    keys.reverse()

    for i in range(1, len(cipher_bs) // 12 + 1):
        L = cipher_bs[len(cipher_bs) - (i * 12): len(cipher_bs) - (i * 12) + 6]
        R = cipher_bs[len(cipher_bs) - (i * 12) + 6: len(cipher_bs) - (i * 12) + 12]

        for j in range(4):
            temp = bitstring.BitArray(R)

            R = f(R, keys[j]) ^ L

            L = temp

        print("D", L, R)

        plain_bs.append(R)
        plain_bs.append(L)

    return plain_bs

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