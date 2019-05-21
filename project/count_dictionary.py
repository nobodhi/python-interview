# auto count into dictionary

colors = ['red', 'white', 'blue', 'red', 'red', 'white']

d = {}

for color in colors:
  d[color] = d.get(color, 0) + 1

print(d)
print(sorted(d))
for k, v in d.items():
  print(k, v)