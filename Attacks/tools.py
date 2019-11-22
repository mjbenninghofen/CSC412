def frequencyAnalysis(text, doPrint = False):
    count = [0] * 26
    total = 0
    text.lower()

    for t in text:
        total += 1
        if t.isalpha():
            count[ord(t) - 97] += 1

    max = 0
    for i in range(len(count)):
        if count[max] < count[i]:
            max = i
        if doPrint:
            print(i, chr(i + 97), (count[i] / total) * 100)

    if doPrint:
        print("Most common:", chr(max + 97))

    return max
    

def keyLength(ciphertext, offsetSteps, doPrint=False):
    collisions = []
    maxIndex = 0

    if doPrint:
        print("Collisions:")
    # For each displacement
    for i in range(offsetSteps):
        collisions.append(0)
        if doPrint:
            print(i + 1, ": ")

        # and each character in the displaced string
        for j in range(len(ciphertext) - 1 - i):
            if ciphertext[j] == ciphertext[j+i+1]:
                collisions[i] += 1

        if collisions[i] > collisions[maxIndex]:
            maxIndex = i

        if doPrint:
            print(collisions[i])

    return maxIndex + 1
