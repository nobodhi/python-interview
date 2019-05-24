# confirm that a given IP address is valid.

def validate_ip(ip_address):
  l = ip_address.split(".")
  if len(l) != 4:
    return None
  if l[0] == 0:
    return None
  for t in range(0,4):
    if not l[t].isdecimal():
      return None
    elif (int(l[t]) < 0 or int(l[t]) > 255):
      return None
  return l

print(validate_ip('127.0.0.1'))
print(validate_ip('127.0.0.1.4'))
print(validate_ip('127.b.0.1'))

assert validate_ip('127.0.0.1') == ['127', '0', '0', '1']
assert validate_ip('127.0.0.256') == None
assert validate_ip('127.0.a.1') == None
