def GoldRush(n, m):
    # Base cases
    if n == m:
        return True
    if n < m:
        return False
    if n % 2 == 0 and GoldRush(n // 2, m):
        return True
    if m % 2 == 0 and GoldRush(n, m // 2):
        return True
    return True

print(GoldRush(6, 4))  # Output: True
