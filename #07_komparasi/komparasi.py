# Belajar operasi komparasi (untuk membadingkan nilia)

a = 5
b = 7

print("Lebih besar (>)")
hasil = a > b
hasil = b > 5
print(a, '>', b, '=', hasil)
print(b, '>', 5, '=', hasil)

print("Kurang dari (<)")
hasil = a < 7
hasil = b < 5
print(a, '<', 7, '=', hasil)
print(b, '<', 5, '=', hasil)

print("Lebih besar sama dengan (>=)")
hasil = a >= b
hasil = b >= 7
print(a, '>=', b, '=', hasil)
print(b, '>=', 7, '=', hasil)


print("Kurang dari sama dengan (<=)")
hasil = a <= b
hasil = b <= 5
print(a, '<=', 7, '=', hasil)
print(b, '<=', 5, '=', hasil)

print("sama dengan (==)")
hasil = a == b
hasil = b == 5
print(a, '==', 7, '=', hasil)
print(b, '==', 5, '=', hasil)

print("tidak sama dengan (!=)")
hasil = a != b
hasil = b != 5
print(a, '!=', 7, '=', hasil)
print(b, '!=', 5, '=', hasil)

# is (membandingkan komparasi antara nilai  yang memakan memrory)
print("===== object identity (is)")
x = 10
y = 10
print('nilai x', x, 'id = ', hex(id(x)))
print('nilai y', y, 'id = ', hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

x = 10
y = 10
print('nilai x', x, 'id = ', hex(id(x)))
print('nilai y', y, 'id = ', hex(id(y)))
hasil = x is not y
print("x is not y = ", hasil)
