# sieve of eratosthenes O(n log log n)


def find_primes(max_value):
    """returns every prime up to a given value."""

    # cardinals up to max_value
    numbers = {a: True for a in range(2, max_value+1)}
    # sieve = list(filter(lambda f: f <= max_value**0.5, numbers))
    sieve = [n for n in numbers if n <= max_value**0.5]
    # set to false multiples of primes starting with 2
    for current in sieve:
        if numbers[current]:
            multiple = current**2
            while multiple <= max_value:
                if numbers[multiple]:
                    numbers[multiple] = False
                multiple += current

    # primes = list(filter(lambda p: numbers[p], numbers))
    primes = [p for p in numbers if numbers[p]]
    return primes


print(find_primes(100))
assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
