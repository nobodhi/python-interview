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


# convert an integer to a list of digits without libraries or strings
x = 100
print(x)
loop = 0
digits = []
while x > 0:
    digit = (x // 10**loop) % 10
    digits.append(digit)
    x = x - digit * 10**loop
    print(digit, loop, x, digits)
    loop += 1
length = len(digits)

# convert an integer to a list using strings
y = 100
print(y)
z = list(str(y))
print(z)
z = list(map(int, str(y))) # for integers
print(z)
digits = map(int,list(str(y))) # <map object at 0x000002B7F9049780>
print(digits)