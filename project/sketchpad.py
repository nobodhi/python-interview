import time
start = time.time()

# 9. Find the Pythagorean triplet for which a + b + c = 1000 and return its product.
def pythagorean_triplet(n: int) -> ((int, int, int), int):
    """find the Pythagorean triplet whose sum equal n and return its product. """
    # brute force: we know a + b + c = 1000 and a^2 + b^2 = c^2
    # [((200, 375, 425), 31875000)]
    # return [((a, b, c), a*b*c) for c in reversed(range(n-1))
    #         for b in reversed(range(c))
    #         for a in reversed(range(b))
    #         if a*a + b*b == c*c and a + b + c == n]
    # a + b + c = n and a^2 + b^2 = c^2
    # step 1 find all a, b, c such that a + b + c = n 
    for c in reversed(range(n//2)):
        # print("c", c)
        for b in reversed(range(1, c-1)):
            # print("b", b)
            # at this point "a" is just n - c - b
            a = n - c - b
            print("c", c, "b", b, "a", a)


start = time.time()
print('pythagorean_triplet', pythagorean_triplet(1000)) # e.g. 12. TODO very slow!
print(round(time.time() - start, 2), "seconds elapsed")
