# Belajar operator yitwise (operasi biner)

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("\n =========OR=========")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))

print("-----------------------------(|)")
print("nilai: ", c, ", binary: ", format(c, "08b"))

c = a & b
print("\n =========AND=========")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))

print("-----------------------------(&)")
print("nilai: ", c, ", binary: ", format(c, "08b"))


c = a ^ b
print("\n =========XOR=========")
print("nilai: ", a, ", binary: ", format(a, "08b"))
print("nilai: ", b, ", binary: ", format(b, "08b"))

print("-----------------------------(^)")
print("nilai: ", c, ", binary: ", format(c, "08b"))
