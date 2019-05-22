# ideomatic fibonacci vs recursive
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

val = 15

def fib_l(n):
  if n < 2:
    return 1
  x, y = 1, 1
  for i in range(n):
    x, y = y, x + y
  return x

def fib_r(n):
  if n < 2:
    result = 1
  else:
    result = fib_r(n-1)+fib_r(n-2)
  return result

print(fib_l(val))
print()
print(fib_r(val))

# make a random assertion
assert fib_l(15) == fib_r(15) == 987