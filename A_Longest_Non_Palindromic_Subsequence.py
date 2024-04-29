def longest_non_palindrome(word):
    for i in range(len(word)):
        if word[i+1:] != word[:i:-1]:
            return len(word) - i - 1
    return -1

test = int(input())
for t in range(test):
    word = input()
    print(longest_non_palindrome(word))
