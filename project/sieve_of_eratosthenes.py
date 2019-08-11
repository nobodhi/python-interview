# sieve of eratosthenes O(n log log n)
# NB any smaller multiple of a prime greater than n**2
# will have already been eliminated in a previous pass
# therefore we only need to check primes up to n**0.5.


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


print(find_primes(10001))
# assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
