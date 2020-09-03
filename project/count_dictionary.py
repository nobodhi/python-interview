# combining lists into dictionaries
names = ['x', 'y', 'z']
coords = [[1, 2], [3, 4], [5, 6]]
d = dict(zip(names, coords))
print('zipped dictionary', d)
l = list(zip(names,coords))
print('zipped list', l) # tuples

# using pandas Series to create a dictionary
names = ['x', 'y', 'z']
coords = [[1, 2], [3, 4], [5, 6]]
import pandas as pd
s = pd.Series(index=names, data=coords)
h = dict(s)
print('panda series dictionary', h)

# auto count into dictionary
colors = ['red', 'white', 'blue', 'red', 'red', 'white']
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
# print(d)
# print(d.items())
print("dict items")
for k, v in d.items():
    print(k, v)

# Same thing using Counter
from collections import Counter
counts = Counter(colors)
print(Counter(counts))
print('counter most common', Counter(counts).most_common(1))

# Functional approach (best!)
l = [[x, colors.count(x)] for x in set(colors)]
print('count set', l)


# # merge two dictionaries using **kwargs BAD
# dict1 = {k: True for k in range(10)}
# print(dict1)
# dict2 = {k: True for k in range(10, 20)}
# print(dict2)
# dict3 = {**dict1, **dict2}
# print(dict3)

# # more idiomatic method using builtin fuction GOOD
# dict1 = {k: True for k in range(10)}
# print(dict1)
# dict2 = {k: True for k in range(10, 20)}
# print(dict2)
# dict1.update(dict2)
# print(dict1)

