import time
# start = time.time()
# print(time.time() - start)


def brute_force(n: int) -> ((int, int, int), int):
    """stub"""
    # brute force: we know a + b + c = 1000 and a^2 + b^2 = c^2
    # try every c with every b and then with every a
    return [((a,b,c), a*b*c) for a in range(n+1) for b in range(a) for c in range(b) if a*a == b*b + c*c and a + b + c == n]


start = time.time()
n = 1000
print('brute_force', brute_force(n))
print(time.time() - start)
