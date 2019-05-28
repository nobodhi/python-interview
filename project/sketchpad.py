# that, given an array A of N integers, returns the smallest positive integer 
# (greater than 0) that does not occur in A. Assume A[i] <= 1000000.

def find_smallest(A):
    for index in range(1,1000000):
        if A.count(index) == 0:
            return index
    return None


# example =  [3, 6, 4, 1, 2]
# print(find_smallest(example))

# performing at most one swap operation rearrange the array(list)
# such that the list is in non-decreasing order.
# assume length 100 and A[i} <= 1000000]

# walk thru array sending out a runner looking for last swap partner
# if there is more than one this won't work and we'll return False

def one_swap_away(A):
    swap_found = False
    swap = None
    for index in range(1,len(A)):
        print(A[index],A[index-1])
        if A[index] < A[index-1]: 
            problem_index = index-1
            print("{} is out of order".format(A[problem_index]))
            # send out a runner to find swap partner. there can be only one!
            for runner in range(index,len(A)):
                print("checking {}".format(A[runner]))
                if A[runner] <= A[problem_index]:
                    print("swap found at {}".format(A[runner]))
                    if swap_found and A[runner] > swap:
                        return False
                    else:
                        swap = A[runner]
                        swap_found = True
    return True

# example =  [1,5,3,3,7]
# print(one_swap_away(example))
# example =  [1,3,5,3,4]
# print(one_swap_away(example))


def get_parking_fee(E, L):
    """parking problem
    entrance fee = 2
    first full or partial hour = 3
    successive full or partial hours = 4
    enter at time E
    leave at time L (HH:MM)
    assume E is before L and on the same day
    """
    import math
    entrance_fee = 2
    first_hour_rate = 3
    successive_rate = 4
    successive_hours = 0
    total_fee = entrance_fee
    
    (entry_hour, entry_minute) = E.split(":")
    (exit_hour, exit_minute) = L.split(":")
    time_in = int(entry_hour)*60 + int(entry_minute)
    time_out = int(exit_hour)*60 + int(exit_minute)
    total_fee = entrance_fee
    if (time_out - time_in >= 0):
        total_fee += first_hour_rate
    if (time_out - time_in >= 0):
        successive_hours = math.ceil((time_out - time_in)/60 - 1)
        total_fee += successive_hours * successive_rate
    return total_fee

print(get_parking_fee("10:00", "13:21"))
