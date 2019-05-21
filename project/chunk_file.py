# chunk file

def read_file():
  with open('./data/textfile.txt') as f:
      print (f)
  
def read_lines():
  with open('./data/textfile.txt') as f:
    for line in f:
      print (line)

def chunk_file():
  from functools import partial
  blocks = []
  with open('./data/textfile.txt') as f:
    for block in iter(partial(f.read,32),''):
      blocks.append(block.replace('\n', '##'))
  print(blocks)

def hash_file():
  from functools import partial
  h = {}
  with open('./data/textfile.txt') as f:
    i = 0
    for line in f:
      i += 1
      x,y = line.rstrip('\n').split(",") 
      h[i] = [int(x),int(y)]
  print (h)