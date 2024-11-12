word = input()
expec = int(input())

unique = len(set(word))

if len(word) < expec:
    print("impossible")
else:
    print(max(0, expec - unique))
