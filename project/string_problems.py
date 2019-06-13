# string problems


def is_unique_words(str):
    """returns True if every word in the string is unique"""
    s = str.split()
    for x in set(s):
        if (s.count(x) > 1):
            return False
    return True


def is_unique_chars(str):
    """returns True if every character in the string is unique"""
    s = [char for char in str]
    print(s, str)
    for x in set(s):
        if (s.count(x) > 1):
            print(x)
            return False
    return True


print(is_unique_chars("abba"))
print(is_unique_chars("cat"))


def one_edit_away(word1, word2) -> bool:
    """walk thru both char lists and count differences"""
    list1 = [char for char in word1]
    list2 = [char for char in word2]
    print(list1, list2)
    len1 = len(list1)
    len2 = len(list2)
    same_length = (len1 == len2)
    if abs(len1-len2) > 1:
        return False
    differences = 0
    index1 = index2 = 0
    while index1 < len1 and index2 < len2:
        if list1[index1] != list2[index2]:
            if differences > 0:
                return False
            differences += 1
            if same_length:
                index1 += 1
                index2 += 1
            elif len1 > len2:
                index1 += 1
            else:
                index2 += 1
        index1 += 1
        index2 += 1
    return True



print(one_edit_away("shell", "shill"))
print(one_edit_away("shell", "smell"))
print(one_edit_away("shell", "smells"))
print(one_edit_away("shell", "smelt"))
