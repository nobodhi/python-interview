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

from collections import Counter
counts = Counter(colors)
print(Counter(counts))
print(Counter(counts).most_common(1))
