import math
import json
def generate_primes(limit):
    """Generate primes up to a given limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False
    return [x for x, is_prime in enumerate(sieve) if is_prime]

def get_primes_up_to_sqrt(n):
    """Ensure prime.json contains all primes up to floor(sqrt(n)) and return the list of primes up to floor(sqrt(n))."""
    sqrt_n = math.floor(math.sqrt(n))
    
    try:
        with open("prime.json", "r") as file:
            primes = json.load(file)
    except FileNotFoundError:
        primes = generate_primes(2)
        with open("prime.json", "w") as file:
            json.dump(primes, file)

    if primes[-1] < sqrt_n:
        new_primes = generate_primes(sqrt_n)
        primes = sorted(set(primes + new_primes))
        with open("prime.json", "w") as file:
            json.dump(primes, file)

    return [p for p in primes if p <= sqrt_n]