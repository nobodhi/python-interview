import time
start = time.time()

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


start = time.time()
py_triplet = pythagorean_triplet(1000)
print('pythagorean_triplet', py_triplet)
print(round(time.time() - start, 2), "seconds elapsed")
