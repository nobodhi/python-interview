# sketchpad


def filter_octects(ip_address):
    terms = ip_address.split(".")
    l1 = list(filter(lambda octet: octet.isdecimal(), terms))
    print(l1)
    # splat operator
    l2 = [*filter(lambda octet: octet.isdecimal(), terms)]
    print(l2)


filter_octects('127.0.0.1')
