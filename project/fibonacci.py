# ideomatic fibonacci vs recursive
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

val = 15
# think of it as length of the array vs array index

def fib_l(n):
  """using array length, starting at 1"""
  x, y = 0, 1
  for i in range(n):
    print(y)
    x, y = y, x + y

def fib_r(n):
  """using array index, starting at 0"""
  if n < 2:
    result = 1
  else:
    result = fib_r(n-1)+fib_r(n-2)
  return result

fib_l(val)
print("")
print(fib_r(val-1))