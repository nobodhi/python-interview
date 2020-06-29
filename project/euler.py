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


print('largest_palindrome_number', largest_palindrome_number(100, 1000))


# 5. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def find_sequence_scm(n: int) -> int:
    """finds the smallest number that divides everything from 1 to n"""
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    # this number is a multiple of the LCM.
    for i in range(n, factorial, n):
        if (factorial % i == 0):
            for factor in range(2, n+1):
                if i % factor != 0:
                    break  # not the scm
                if factor == n:
                    return i
    return factorial  # default


print('find_sequence_scm', find_sequence_scm(20))


# 6. Find the difference between the sum of the squares and the square of the sum of the first 100 natural numbers.
def diff_sum_squares(n: int) -> int:
    """difference between the sum of the squares and the square of the sum of the first n naturals"""
    return sum([i for i in range(1, n+1)])**2 - sum([i**2 for i in range(1, n+1)])


print('diff_sum_squares', diff_sum_squares(100))


# 7. What is the 10001st prime number?
def find_nth_prime(n: int) -> int:
    """modified sieve checks every natural number against all previous primes to find the nth prime"""
    assert n >= 2
    current = 3
    primes = [current]
    if n == 1:
        return current
    # add 1 continuously in a loop checking if the number divides any of the previously found primes
    while len(primes) < n:
        if current == 2:
            current += 1
        else:
            current += 2
        is_prime = True
        for prime in primes:
            if current % prime == 0:
                is_prime = False
                break  # not a prime
        if is_prime:
            primes.append(current)
            # print(primes)
    return primes[-1]


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
    import math
    for c in reversed(range(int(math.sqrt(n)), n//2)):
        for b in reversed(range(1, c)):
            a = n - c - b
            if a > c:
                break
            # print("c", c, "b", b, "a", a)
            if (c**2 == a**2 + b**2):
                return (a, b, c), a*b*c

# [((200, 375, 425), 31875000)]
print('pythagorean_triplet', pythagorean_triplet(1000))

# 10. Find the sum of the primes less than two million.

def sum_of_primes(n: int) -> int:
    """return the sum of all primes less than n"""
    # just find every prime using erastosthenes, and tally as you find them
    return sum(find_primes(n))

def find_primes(max_value):
    """returns every prime up to a given value."""

    # NOTE: dict is exponentially faster than list
    numbers = {a: True for a in range(2, max_value+1)}
    sieve = [n for n in numbers if n <= max_value**0.5]
    for current in sieve:
        if numbers[current]:
            prime_multiple = current**2
            while prime_multiple <= max_value:
                if numbers[prime_multiple]:
                    numbers[prime_multiple] = False
                prime_multiple += current
    primes = [p for p in numbers if numbers[p]]
    return primes

print('sum_of_primes', sum_of_primes(2000000))

# 11. Find the maximum product of four adjacent numbers in a 20x20 matrix.

def matrix_search(my_list: list) -> int:
    import numpy as np
    arr = np.array(my_list)
    (x, y) = arr.shape
    # print(arr)
    return crawl_matrix(arr, x) 

def crawl_matrix(arr, n):
    import numpy as np
    max_product = 0
    for x in range(n):
        for y in range(n):
            perform_vertical_check = False
            if (x+3 <= n-1):
                perform_vertical_check = True
                max_product = check_vertical(arr, x, y, max_product)
                if (y-3 >= 0):
                    max_product = check_backward_diag(arr, x, y, max_product)
            if (y+3 <= n-1):
                max_product = check_horizontal(arr, x, y, max_product)
                if (perform_vertical_check): 
                    max_product = check_forward_diag(arr, x, y, max_product)
    return max_product

def check_vertical(arr, x, y, max_product):
    product = arr[x,y]
    for i in range(x+1, x+4):
        product *= arr[i, y]
        if (product > max_product):
            max_product = product
            # print("vertical", x, y, arr[x,y], "max_product", max_product)
    return max_product

def check_backward_diag(arr, x, y, max_product):
    product = arr[x, y]
    j = y
    for i in range(x+1, x+4):
        j -= 1
        product *= arr[i, j]
        if (product > max_product):
            max_product = product
            # print("back diag", x, y, arr[x,y], "max_product", max_product)
    return max_product

def check_horizontal(arr, x, y, max_product):
    product = arr[x, y]
    for j in range(y+1, y+4):
        product *= arr[x, j]
        if (product > max_product):
            max_product = product
            # print("horizontal", x, y, arr[x,y], "max_product", max_product)
    return max_product

def check_forward_diag(arr, x, y, max_product):
    product = arr[x, y]
    j = y
    for i in range(x+1, x+4):
        j += 1
        product *= arr[i, j]
        if (product > max_product):
            max_product = product
            # print("fwd diag", x, y, arr[x,y], "max_product", max_product)
    return max_product

my_matrix = [
[ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
[52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
[24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
[16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],
[86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
[ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
[20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
[ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]
]

print("matrix max product", matrix_search(my_matrix))
