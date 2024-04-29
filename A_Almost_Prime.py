# def almost_prime(n):
#     count = 0
#     def trial_division_simple(n: int) -> list[int]:
#         factorization: list[int] = []
#         d = 2
#         while d * d <= n:
#             while n % d == 0:
#                 factorization.append(d)
#                 n //= d
#             d += 1
#             if n > 1:
#                 factorization.append(n)
#         print(factorization)

#         return len(factorization) == 2
#     for i in range(2, n+1):
#         if trial_division_simple(i):
#             count += 1
#     return count

# print(trial_division_simple(3000))
def almost_prime(n):
    count = 0
    
    def prime_factors_count(num):
        count = 0
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                count += 1
                while num % divisor == 0:
                    num //= divisor
            divisor += 1
        if num > 1:
            count += 1
        return count
    
    for i in range(2, n+1):
        if prime_factors_count(i) == 2:
            count += 1
    
    return count

n = int(input())
print(almost_prime(n))
