def smallest_common_multiple(n: int) -> int:
    """finds the smallest number that divides everything from 1 to n"""
    if n <= 2:
        return n
    current = 2*n
    # outer loop: iterate "current" upwards searching for the SCM
    while True:
        if n > 4 and current % 10 != 0:
            current = n//10 * 10 + 10
        # inner loop: iterate "i" checking for divisibility
        for i in range(3, n+1):
            # print(current, i)
            if current % i != 0:
                break
            else:
                if i == n:
                    return current
        if n <= 4:
            current += 2
        else:
            current += 10


# What is the smallest positive integer evenly divisible by all integers less than 20?
# Better LCM solutions include prime factorization, GCD, and sieve.
def find_scm(n: int) -> int:
    """finds the smallest number that divides everything from 1 to n"""
    sum = 1
    for i in range(1, n+1):
        sum*=i
    # print(i, sum)
    # this number is a multiple of the LCM.
    for i in range(n, sum//2, n):
        if (sum % i == 0):
            for factor in range(3, n+1):
                if i % factor != 0:
                    break # not the scm
                if factor == n:
                    return i
    return sum # default

n = 20
# print('smallest_common_multiple', smallest_common_multiple(n))
print('find_scm', find_scm(n))
