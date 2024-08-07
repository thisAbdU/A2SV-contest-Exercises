def diff_string(s):
    ls_ = list(s)

    if len(set(ls_)) == 1:
        print("NO")
        return
    
    j = 0
    for i in range(len(ls_)):
        if ls_[i] != s[j]:
            ls_[i], ls_[j] = ls_[j], ls_[i]
            break
    print("YES")
    print("".join(ls_))
    return


test = int(input())
for t in range(test):
    s = input()
    diff_string(s)