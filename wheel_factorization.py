import math
from math import gcd

def generate_wheel_primes(base1, base2, limit):
    wheel_period = math.lcm(base1, base2)
    wheel_iterations = (limit // wheel_period) + 1
    non_zero_remainders = []
    wheel_prime_candidates = [base1, base2]
    
    for i in range(1, wheel_period):
        if gcd(wheel_period, i) == 1:
            non_zero_remainders.append(i)
            if i != 1:
                wheel_prime_candidates.append(i)
    
    for i in range(1, wheel_iterations):
        for remainder in non_zero_remainders:
            wheel_prime_candidates.append((wheel_period * i) + remainder)

    return wheel_prime_candidates

def wheel_factorization(n, base1=2, base2=3):
    """Perform factorization using the Wheel Factorization algorithm with base1 and base2 bases."""
    # Step 1: Generate wheel primes based on the gcd of base1 and base2
    wheel_prime_candidates = generate_wheel_primes(base1, base2, int(math.sqrt(n)) + 1)
    # Step 2: Test divisibility for numbers in the wheel
    factors = []
    for prime in wheel_prime_candidates:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
        if n == 1:
            break

    return factors

n=2121
print(f'Factors of {n} are {wheel_factorization(n)}')