def count_correct(n, ans):
    arr = []

    arr.append(ans.count('A'))
    arr.append(ans.count('B'))
    arr.append(ans.count('C'))
    arr.append(ans.count('D'))

    total = 0

    for i in arr:
        if i > n:
            total += n
        else:
            total += i
    return total


test = int(input())
for _ in range(test):
    n = int(input())
    s = input()
    print(count_correct(n, s))