# string problems


def is_unique(str):
    """returns True if every word in the string is unique"""
    s = str.split()
    for x in set(s):
        if (s.count(x) > 1):
            return False
    return True
