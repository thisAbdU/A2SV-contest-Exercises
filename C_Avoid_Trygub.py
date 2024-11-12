CONST = "trygub"
for _ in range(int(input())):
    n = int(input())
    word = list(input())

    res = []
    not_res = []
    i = 0
    while i < n:
        if word[i] == 'b':
            res.append("b")
        else:
            not_res.append(word[i])

        i += 1

    res = res[:] + not_res[:]
    print("".join(res))