# ideomatic fibonacci vs recursive
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fib(n):
    """the pythonic approach"""
    if n < 2:
        return 1
    x, y = 1, 1
    for _ in range(n):
        # print(_, x, y)
        x, y = y, x + y
    return x


def fib_recursive(n, memo={}):
    """recursive fibonacci reaches maximum recursion after 998 calls"""
    if n in memo:
        return memo[n]
    if n < 2:
        result = 1
    else:
        result = fib_recursive(n-1, memo)+fib_recursive(n-2, memo)
    memo[n] = result
    return result


val = 998
print(fib(val))
print()
print(fib_recursive(val))

# make a random assertion
assert fib(15) == fib_recursive(15) == 987
