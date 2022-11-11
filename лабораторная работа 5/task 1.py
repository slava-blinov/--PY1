from pprint import pprint

# TODO решить с помощью list comprehension и распечатать его
slovari = [{"bin": bin(x), "dec": x, "oct": oct(x), "hex": hex(x)} for x in range(16)]

pprint(slovari)
