def frequencyAnalysis(text):
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
        print(i, chr(i + 97), (count[i] / total) * 100)

    print("Most common:", chr(max + 97))