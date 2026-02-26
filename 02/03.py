'''
列表推导同filter和map的比较
'''

symbols = '$%^&*'
beyond_ascii = [ord(s) for s in symbols if ord(s)> 1]
print(beyond_ascii)


# a1 = list(map(ord, symbols))
a1 = list(filter(lambda c: c> 1, map(ord, symbols)))
print(a1)