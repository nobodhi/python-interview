# sieve of eratosthenes O(n log log n)


def find_primes(max_value):
    """naive solution. check every cardinal number for prime multiples."""

    # cardinals up to max_value
    candidates = {a: True for a in range(2, max_value+1)}
    # sieve = list(filter(lambda f: f <= max_value**0.5, candidates))
    sieve = [candidate for candidate in candidates if candidate <= max_value**0.5]

    for current in sieve:
        if candidates[current]:
            runner = current**2
            while runner <= max_value:
                if candidates[runner]:
                    candidates[runner] = False
                runner += current

    primes = list(filter(lambda p: candidates[p], candidates))
    return primes


print(find_primes(100))
assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
