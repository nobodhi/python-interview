import numpy as np

def random_list(length):
    """returns a random list of integers from 1 to 100"""
    unsorted = list(np.random.randint(100, size=length))
    return unsorted

# TODO sequential_array 

def sequential_array(length):
    """return arange sequence, which we then square and reshape"""
    array = np.arange(0, length**2).reshape(length, length).tolist()
    return array

def random_array(length):
    """return a square matrix of random integers from 1 to 100"""
    array = np.random.randint(1,100,length**2).reshape(length, length).tolist()
    return array

# print(list(sequential_array(10)))
print(random_array(10))