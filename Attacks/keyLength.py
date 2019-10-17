import sys

def main(argv):
    if len(argv) != 3:
        print("Usage: KeyLength.py <number of offset steps> <ciphertext>")
        sys.exit()

    num = int(argv[1])
    t1 = argv[2]

    collisions = []

    print("Collisions:")
    # For each displacement
    for i in range(num):
        collisions.append(0)
        print(i + 1, ": ", end='')
        # and each character in the displaced string
        for j in range(len(t1) - 1 - i):
            if t1[j] == t1[j+i+1]:
                collisions[i] += 1
        print(collisions[i])

    #for i in range(26):
    #    print(i, chr(97 + i))


if __name__ == "__main__":
    main(sys.argv)
