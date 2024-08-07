def slavic_exam(s, t):
    tt = ""
    for l in s:
        if l in t:
            tt += l
    print("tt", tt)


for _ in range(int(input())):
    s = input()
    t = input()
    slavic_exam(s, t)


