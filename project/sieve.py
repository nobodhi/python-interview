# sieve of eratosthenes

def find_primes(max_value):
  # candidate values: all the cardinals up to max_value
  # filter values: the primes less than sqrt(max_value)

  candidates = {a:True for a in range(2,max_value+1)}
  filters = list(range(2,int(max_value**0.5)+1)) 

  for current in filters:
    if candidates[current]:
      runner = current**2
      while runner <= max_value:
        if candidates[runner]:
          candidates[runner] = False
        runner += current 

  primes = {k:v for (k,v) in candidates.items() if v == True}
  return list(primes.keys())

print(find_primes(100))
# assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
