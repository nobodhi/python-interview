import time
start = time.time()
print(time.time() - start)

def sum_of_primes(n: int) -> int:
    """return the sum of all primes less than n"""
    # just find every prime using erastosthenes, and tally as you find them
    return sum(find_primes(n))

def find_primes(max_value):
    """returns every prime up to a given value."""

    # NOTE: dict is exponentially faster than list
    numbers = {a: True for a in range(2, max_value+1)}
    # sieve = list(filter(lambda f: f <= max_value**0.5, numbers))
    sieve = [n for n in numbers if n <= max_value**0.5]
    for current in sieve:
        if numbers[current]:
            prime_multiple = current**2
            while prime_multiple <= max_value:
                if numbers[prime_multiple]:
                    numbers[prime_multiple] = False
                prime_multiple += current
    # primes = list(filter(lambda p: numbers[p], numbers))
    primes = [p for p in numbers if numbers[p]]
    return primes


start = time.time()
n = 2000000
print('sum_of_primes', sum_of_primes(n))
print(time.time() - start)
