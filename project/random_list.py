import numpy as np

def random_list(length):
    """returns a random list of integers of length n"""
    unsorted = list(np.random.randint(100, size=length))
    return unsorted
