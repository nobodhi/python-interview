# project euler https://projecteuler.net/

# https://projecteuler.net/problem=1
# find the sum of all positive integers less than 1000 that are multiples of 3 or 5
sum([(num % 3 == 0 or num % 5 == 0)*num  for num in range(1,1000)])

