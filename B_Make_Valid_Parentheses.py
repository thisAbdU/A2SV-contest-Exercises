from collections import deque


def valid_parenthesis(bracket):
    stack = deque()
    count = 0
    for i in bracket:
        if i == "(":
            stack.append(i)
        elif stack and i == ")":
            stack.pop()
            count += 2
    return count


bracket = input()
print(valid_parenthesis(bracket))


    