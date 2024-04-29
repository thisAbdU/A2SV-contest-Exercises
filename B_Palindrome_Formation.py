def palindrome_formation(len_s, string_):
    def palindrome_check(string_, i):
        return string_[i] == string_[len_s - i - 1]

    # Iterate through the first half of the string
    for i in range(1, len_s // 2):
        j = i - 1
        if palindrome_check(string_, i) == True and palindrome_check(string_, j) == False:
            return "No"
        elif palindrome_check(string_, i) == False and palindrome_check(string_, j) == True:
            return "No"
        
    return "Yes"

# Read the number of test cases
test_case = int(input())

# Iterate through each test case
for _ in range(test_case):
    len_ = int(input())
    string_ = input()
    print(palindrome_formation(len_, string_))
