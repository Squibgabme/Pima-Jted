import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_up_to_N(N):
    primes = [2, 3]
    for num in range(5, N + 1, 6):
        if is_prime(num):
            primes.append(num)
        if is_prime(num + 2):
            primes.append(num + 2)
    for prime in primes:
        print(prime)

# Continuous looping until the user decides to exit
while True:
    N = int(input("Enter the value of N (enter 0 to exit): "))
    if N == 0:
        break
    print("Prime numbers from 1 to", N, "are:")
    print_primes_up_to_N(N)
