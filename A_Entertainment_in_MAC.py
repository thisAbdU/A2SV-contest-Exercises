def entertainment(n: int, s:str) -> str:
    for i in range(len(s)):
        if n%2 == 0:
            if ord(s[i]) > ord(s[len(s) - i -1]):
                return s[::-1] + s
            elif ord(s[i]) < ord(s[len(s) - i -1]):
                return s
        else:
            if ord(s[i]) > ord(s[len(s) - i -1]):
                return s[::-1] + s
            elif ord(s[i]) < ord(s[len(s) - i -1]):
                return s + s[::-1]
    return s

testCase = int(input())
for i in range(testCase):
    n = int(input())
    s = input()
    print(entertainment(n, s))