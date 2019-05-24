# sieve of eratosthenes O(n log log n)

def find_primes(max_value):
  """naive solution. check every cardinal number for prime multiples.
  TODO: a wheel sieve only looks at those cardinals ending in 1,3,7,9"""

  candidates = {a:True for a in range(2,max_value+1)} # cardinals up to max_value
  filters = list(range(2,int(max_value**0.5)+1)) # primes up to sqrt(max_value)
  counter = max_value + int(max_value**0.5)+1 # count of bit operations

  for current in filters:
    if candidates[current]:
      runner = current**2
      counter+=1
      while runner <= max_value:
        if candidates[runner]:
          counter += 1
          candidates[runner] = False
        runner += current 
        counter += 1

  primes = [k for (k,v) in candidates.items() if v == True]
  counter += len(primes)
  print("max ", max_value, "operations ", counter)
  return primes

print(find_primes(100))
# assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
