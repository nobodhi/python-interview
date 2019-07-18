# project euler https://projecteuler.net/


# find the sum of all positive integers less than 1000 that are multiples of 3 or 5
def sum_mulitples(x, y, n):
    """find the sum of all multiples of x and y less than n"""
    return sum([(num % x == 0 or num % y == 0)*num for num in range(1, n)])


print('sum_mulitples', sum_mulitples(3, 5, 1000))


# find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
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


# What is the largest prime factor of the number 600851475143?
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


# what is the largest palindromic number that is the product of two 3 digit numbers?
def largest_palindrome_number(lo, hi):
    result = 0
    for i in reversed(range(lo, hi)):
        for j in reversed(range(lo, hi)):
            val = list(str(i*j))
            # print(i, j, val)
            palindrome = True
            for k in range(len(val)//2 + 1):
                # print(i, j, k, val, val[k], val[len(val)-1-k])
                if val[k] != val[len(val)-1-k]:
                    palindrome = False
                    break
            if palindrome == True:
                # print(i, j, val)
                if i*j > result:
                    result = i*j
    return result
# 111**2 = 12321

print(largest_palindrome_number(100, 1000))