import time
# start = time.time()
# print(time.time() - start)


def brute_force(n: int) -> ((int, int, int), int):
    """stub"""
    # brute force: we know a + b + c = 1000 and a^2 + b^2 = c^2
    return n


start = time.time()
n = 1000
print('brute_force', brute_force(n))
print(time.time() - start)
