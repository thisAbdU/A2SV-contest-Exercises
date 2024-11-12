import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(limit):
    for num in range(2, limit + 1):
        is_prime(num)

if __name__ == "__main__":
    limit = 100000  # Adjust this limit as needed
    start_time = time.time()
    find_primes(limit)
    end_time = time.time()
    print("Execution Time in Python: {:.6f} seconds".format(end_time - start_time))
