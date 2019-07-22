# derp

# the smallest number than evenly divides all integers less than n
def smallest_common_multiple(n: int) -> int:
    """finds the smallest number that divides everything from 1 to n"""
    # outer loop: iterate index upwards searching for the SCM
    if n <= 2:
        return n
    current = 2*n
    while True:
        if n > 4 and current % 10 != 0:
            current+=2
        else:
            for index in range(3, n+1):
                if current % index != 0:
                    break
                else:
                    if index == n:
                        return current
            if n <= 4:
                current+=2
            else:
                current+=10

print(smallest_common_multiple(10))
print(smallest_common_multiple(20)) 

