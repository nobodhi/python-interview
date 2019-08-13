# project euler https://projecteuler.net/


# 1. Find the sum of all positive integers less than 1000 that are multiples of 3 or 5
def sum_mulitples(x, y, n):
    """find the sum of all multiples of x and y less than n"""
    return sum([(num % x == 0 or num % y == 0)*num for num in range(1, n)])


print('sum_mulitples', sum_mulitples(3, 5, 1000))


# 2. Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
def sum_even_fibonacci(n):
    """sum of the even-valued terms of the fibonacci sequence not exceeding n"""
    result = 0
    if n >= 2:
        x, y = 1, 1
        for _ in range(n):
            x, y = y, x + y
            if x > n:
                break
            if x % 2 == 0:
                # print(x, y)
                result += x
    return result


print('sum_even_fibonacci', sum_even_fibonacci(4000000))


# 3. What is the largest prime factor of the number 600851475143?
def largest_prime_factor(n):
    """find the largest prime factor of n"""
    # NOTE 600851475143 is way too big to find every possible factor quickly.
    # we must divide n by every "prime" starting from 2.
    current = 2
    max_factor = n
    while current < max_factor:
        while max_factor % current == 0:
            max_factor = max_factor//current
            # print(current, max_factor)
        if current % 2 == 0:
            current += 1
        else:
            current += 2
    return max_factor


print('largest_prime_factor', largest_prime_factor(600851475143))


# 4. What is the largest palindromic number that is the product of two 3 digit numbers?
def largest_palindrome_number(lo, hi):
    """largest palindromic product within a given range (using strings)"""
    result = 0
    for i in reversed(range(lo, hi)):
        for j in reversed(range(lo, hi)):
            val = list(str(i*j))
            # print(i, j, val)
            is_palindrome = True
            for k in range(len(val)//2 + 1):
                # print(i, j, k, val, val[k], val[len(val)-1-k])
                if val[k] != val[len(val)-1-k]:
                    is_palindrome = False
                    break
            if is_palindrome:
                # print(i, j, val)
                if i*j > result:
                    result = i*j
    return result
# 111**2 = 12321


print('largest_palindrome_number', largest_palindrome_number(10, 100))
# print('largest_palindrome_number', largest_palindrome_number(100, 1000))


# 5. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# SLOW. O(n!)
def find_sequence_scm(n: int) -> int:
    """finds the smallest number that divides everything from 1 to n"""
    factorial = 1
    for i in range(2, n+1):
        factorial*=i
    # print(i, factorial)
    # this number is a multiple of the LCM.
    for i in range(n, factorial, n):
        if (factorial % i == 0):
            for factor in range(2, n+1):
                if i % factor != 0:
                    break # not the scm
                if factor == n:
                    return i
    return factorial # default


print('find_sequence_scm', find_sequence_scm(20))


# 6. Find the difference between the sum of the squares and the square of the sum of the first 100 natural numbers.
def diff_sum_squares(n: int) -> int:
    """difference between the sum of the squares and the square of the sum of the first n naturals"""
    return sum([i for i in range(1, n+1)])**2 - sum([i**2 for i in range(1, n+1)])


print('diff_sum_squares', diff_sum_squares(100))


# 7. What is the 10001st prime number?
# SLOW
def find_nth_prime(n: int) -> int:
    """modified sieve checks every natural number against all previous primes to find the nth prime"""
    assert n >= 1
    current = 2
    primes = [current]
    if n == 1:
        return current
    # add 1 continuously in a loop checking if the number divides any of the previously found primes
    while len(primes) < n:
        current += 1
        is_prime = True
        for prime in primes:
            if current % prime == 0:
                is_prime = False
                break  # not a prime
        if is_prime:
            primes.append(current)
            # print(primes)
    return primes[-1]


# print('find_nth_prime', find_nth_prime(1001))
print('find_nth_prime', find_nth_prime(10001))


# 8. Find thirteen adjacent digits in the 1000-digit number that have the greatest product
def greatest_sequence_product(val: int, n: int) -> (int, list):
    """given an integer find the subsequence of a given length having the greatest product"""
    digits = list(map(int, str(val)))
    max_product = 0
    for index in range(len(digits)):
        sequence = digits[index:index+n]
        if len(sequence) < n:
            break
        product = digits[index]
        for s in sequence[1:n]:
            product *= s
        if max_product < product:
            max_product = product
        # print(index, sequence, product, max_product)
    return max_product, sequence


# val = 1234567890
val = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
print('greatest_sequence_product', greatest_sequence_product(val, 13))  # 13


# 9. Find the Pythagorean triplet for which a + b + c = 1000 and return its product.
def pythagorean_triplet(n: int) -> ((int, int, int), int):
    """find the Pythagorean triplet whose sum equal n and return its product. """
    return ((n, n, n), n)


print('pythagorean_triplet', pythagorean_triplet(1000))
