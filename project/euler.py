# project euler https://projecteuler.net/

# https://projecteuler.net/problem=1
# find the sum of all positive integers less than 1000 that are multiples of 3 or 5
def sum_mulitples(x, y, n):
    """find the sum of all multiples of x and y less than n"""
    return sum([(num % x == 0 or num % y == 0)*num  for num in range(1,n)])

print(sum_mulitples(3, 5, 1000))

# https://projecteuler.net/problem=2
# find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.
def sum_fibonacci(n):
    """sum of the even-valued terms of the fibonacci sequence not exceeding n"""
    if n < 2:
        return 1
    # we need to create a summand
    x, y = 1, 1
    result = 0
    for _ in range(n):
        x, y = y, x + y
        if x > n: break
        if x % 2 == 0: 
            print(x, y)
            result += x
    return result

print(sum_fibonacci(4000000))
