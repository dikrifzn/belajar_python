##mengcopy suatu list
a = ["michael", "ini", "otong"]

b = a #dengan cara ini kita hanya membuat alternatif variable untuk list

print("a = ", a)
print("b = ", b)

b[0] = "dikrr"

print("a = ", a)
print("b = ", b)

print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")

#untuk mengcopy list dengan full ialah dengan .copy()
c = a.copy()
print("c = ", c)

print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")
print(f"adress C = {hex(id(c))}")

print("a = ", a)
print("b = ", b)
print("c = ", c)