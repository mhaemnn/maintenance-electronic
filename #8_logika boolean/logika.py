# Belajar operasi logika atau boolean (NOT, OR, AND, XOR)

# NOT
a = True
c = not a
print('data a: ', a)
print("--------NOT")
print('data c: ', c)

# OR (jika salah satunya True maka akan Tru)
print("========OR========")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)
# AND (jika salah satunya True maka akan False)
print("========AND========")
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)
# XOR (jika dua-duanya True maka akan False)
print("========XOR========")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)
