# confirm that a given IP address is valid.

def validate_ip(ip_address):
  """An IP address consists of 32 bits, shown as 4 terms 
  of numbers from 0-255 represented in decimal form """

  terms = ip_address.split(".")
  if len(terms) != 4:
    return None
  for octet in range(0,4):
    if not terms[octet].isdecimal():
      return None
    elif (int(terms[octet]) < 0 or int(terms[octet]) > 255):
      return None
  return terms

print(validate_ip('127.0.0.1'))
print(validate_ip('127.0.0.1.4'))
print(validate_ip('127.b.0.1'))

assert validate_ip('127.0.0.1') == ['127', '0', '0', '1']
assert validate_ip('127.0.0.256') == None
assert validate_ip('127.0.a.1') == None
