# Or (Salah Satu True maka hasil True)
print("===OR===")
a = False
b = False
hasil = a ^ b
print(a, "OR", b, "=", hasil)

a = False
b = True
hasil = a ^ b
print(a, "OR", b, "=", hasil)

a = True
b = False
hasil = a ^ b
print(a, "OR", b, "=", hasil)

a = True
b = True
hasil = a ^ b
print(a, "OR", b, "=", hasil)

#AND (jika salah satunya false maka false)
print("===AND===")
a = False
b = False
hasil = a and b
print(a, "OR", b, "=", hasil)

a = False
b = True
hasil = a and b
print(a, "OR", b, "=", hasil)

a = True
b = False
hasil = a and b
print(a, "OR", b, "=", hasil)

a = True
b = True
hasil = a and b


#XOR (akan true jika salah satunya true, sisanya false)
print(a, "XOR", b, "=", hasil)

print("===XOR ===")
a = False
b = False
hasil = a ^ b
print(a, "XOR", b, "=", hasil)

a = False
b = True
hasil = a ^ b
print(a, "XOR", b, "=", hasil)

a = True
b = False
hasil = a ^ b
print(a, "XOR", b, "=", hasil)

a = True
b = True
hasil = a ^ b
print(a, "XOR", b, "=", hasil)