def special_character(n):
    if n%2 != 0:
        return "NO"
    else:
        output = ""
        for i in range(0, n//2):
            output += "A" * 2 + "B"
        print("YES")
        return output

test = int(input())
for t in range(test):
    n = int(input())
    print(special_character(n))
