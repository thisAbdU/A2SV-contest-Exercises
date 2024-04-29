from collections import Counter


def vlad_and_the_best(s):
    freq = Counter(s)

    if freq["A"] > freq["B"]:
        return "A"
    else:
        return "B"

test = int(input())
for tes in range(test):
    s = input()
    print(vlad_and_the_best(s))