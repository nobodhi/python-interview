# confirm that a given IP address is valid.

# naive solution
def validate_ip(ip_address):
  """An IP address consists of 32 bits, shown as 4 terms 
  of numbers from 0-255 represented in decimal form """

  terms = ip_address.split(".")
  if len(terms) != 4:
    return False
  for octet in range(0,4):
    if not terms[octet].isdecimal():
      return False
    elif (int(terms[octet]) < 0 or int(terms[octet]) > 255):
      return False
  return True

print(validate_ip('127.0.0.1'))
print(validate_ip('127.0.0.1.4'))
print(validate_ip('127.b.0.1'))

assert validate_ip('127.0.0.1') == True
assert validate_ip('127.0.0.256') == False
assert validate_ip('127.0.a.1') == False

# filter function BAD
def filter_octects(ip_address):
  """functional approach filters the list"""
  terms = ip_address.split(".")
  if not len([*filter(lambda octet: octet.isdecimal(), terms)])==4:
    return False
  elif not len([*filter(lambda octet: 0<=int(octet)<=255, terms)])==4:
    return False
  else:
    return True

print(filter_octects('127.0.0.1'))

assert filter_octects('127.0.0.1') == True
assert filter_octects('127.0.0.256') == False
assert filter_octects('127.0.a.1') == False

# list comprehension (best!)
def all_valid(ip_address):
  """
  `all` uses list comprehension to filter
  https://docs.python.org/3/library/functions.html#all
  """
  terms = ip_address.split(".")
  if not all(octet.isdecimal() for octet in terms):
    return False
  elif not all(0 <= int(octet) <= 255 for octet in terms):
    return False
  else:
    return True

print(all_valid('127.0.0.1'))

assert all_valid('127.0.0.1') == True
assert all_valid('127.0.0.256') == False
assert all_valid('127.0.a.1') == False
