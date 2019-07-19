# derp

# convert an integer to a list of digits without libraries or strings
x = 100
print(x)
loop = 0
digits = []
while x > 0:
    digit = (x // 10**loop) % 10
    digits.append(digit)
    x = x - digit * 10**loop
    print(digit, loop, x, digits)
    loop += 1
length = len(digits)

# convert an integer to a list using strings
y = 100
print(y)
z = list(map(int, str(y)))
print(z)