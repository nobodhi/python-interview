# combining lists into dictionaries

from collections import Counter
names = ['x', 'y', 'z']
coords = [[1, 2], [3, 4], [5, 6]]

d = dict(zip(names, coords))
print(d)

# auto count into dictionary

colors = ['red', 'white', 'blue', 'red', 'red', 'white']

d = {}

for color in colors:
    d[color] = d.get(color, 0) + 1

print(d)
print(d.items())
for k, v in d.items():
    print(k, v)

# Same thing using Counter

counts = Counter(colors)
print(Counter(counts))
print(Counter(counts).most_common(1))

# Functional approach (best!)

l = [[x, colors.count(x)] for x in set(colors)]

print(l)


# merge two dictionaries using **kwargs
dict1 = {k: True for k in range(10)}
print(dict1)
dict2 = {k: True for k in range(10, 20)}
print(dict2)
dict3 = {**dict1, **dict2}
print(dict3)

# more ideomatic method using builtin fuction
dict1 = {k: True for k in range(10)}
print(dict1)
dict2 = {k: True for k in range(10, 20)}
print(dict2)
dict1.update(dict2)
print(dict1)
