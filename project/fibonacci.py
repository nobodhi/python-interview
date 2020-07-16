# ideomatic fibonacci vs recursive
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fib(n):
    """the pythonic approach - hack the first x value to be 0"""
    x, y = 0, 1
    for _ in range(n):
        # print(_, x, y)
        x, y = y, x + y
    return x

 
def fib_recursive(n, memo={}):
    """recursive fibonacci reaches maximum recursion after 998 calls"""
    if n in memo:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib_recursive(n-1, memo)+fib_recursive(n-2, memo)
    memo[n] = result
    return result


val = 10
print(fib(val))
print()
print(fib_recursive(val))

# make a random assertion
assert fib(10) == fib_recursive(10) == 55
