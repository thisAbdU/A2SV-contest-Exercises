s = input()
res = []
if s[0] == '+':
    res.append(1)
else:
    res.append(-1)
for i in range(1, len(s)):
    if s[i] == '+':
        res.append(res[i-1] + 1)
    else:
        res.append(res[i-1] - 1)

print(res.index(max(res)) + 1)