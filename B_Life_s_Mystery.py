from collections import deque

stack_main = deque()
stack_helper = deque()
Word = input()
for letter in Word:
    if stack_main and stack_main[-1] == letter:
        stack_helper.append(letter)
        while stack_main and stack_main[-1] == stack_helper[-1]:
            stack_main.pop()
    else:
        stack_main.append(letter)
print("".join(stack_main))