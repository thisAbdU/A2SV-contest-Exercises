def is_excellent_number(n):
    from itertools import product
    for digits in product('15', repeat=n):
        number = int(''.join(digits))
        
        digit_sum = sum(int(digit) for digit in digits)
        
        if digit_sum % 3 == 0:
            return number  
    
    return -1  


N = int(input())
result = is_excellent_number(N)

if result != -1:
    print(result)
else:
    print(-1)
