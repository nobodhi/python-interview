# sieve of eratosthenes O(n log log n)


def find_primes(max_value):
    """naive solution. check every cardinal number for prime multiples.
    TODO: a wheel sieve only looks at those cardinals ending in 1,3,7,9"""

    # cardinals up to max_value
    candidates = {a: True for a in range(2, max_value+1)}
    sieves = list(filter(lambda f: f <= max_value**0.5, candidates))

    for current in sieves:
        if candidates[current]:
            runner = current**2
            while runner <= max_value:
                if candidates[runner]:
                    candidates[runner] = False
                runner += current

    primes = list(filter(lambda p: candidates[p], candidates))
    return primes


print(find_primes(100))
# assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
