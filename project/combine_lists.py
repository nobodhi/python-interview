# combining lists into dictionaries

names = ['x', 'y', 'z']
coords = [[1,2],[3,4],[5,6]]

d = dict(zip(names, coords))
print(d)