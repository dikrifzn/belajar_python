data_0 = [1,2]
data_1 = [3,4]
data_2d = [data_0, data_1]

print("data 2d = ", data_2d)

#mengambil data nested list
data_ambil = data_2d[0][0]
print(f"data ambil = {data_ambil}")

#addres nested list copy()
data_2d_copy = data_2d.copy()
print(f"adress asli = {hex(id(data_2d))}")
print(f"adress copy = {hex(id(data_2d_copy))} \n")

print(f"adress member 0 = {hex(id(data_2d[0]))}")
print(f"adress member 0 = {hex(id(data_2d_copy[0]))} \n")
#copy() pada nested list hanya mengcopy luarnya saja (shallow copy), sedangkan list yang ada di dalamnya tidak akan tercopy


#deepcopy
#mengcopy dengan tools deepcopy() dari library copy untuk mengcopy secara mendalam dari list

from copy import deepcopy

data_2d_deepcopy = deepcopy(data_2d)
print(f"adress asli = {hex(id(data_2d))}")
print(f"adress copy = {hex(id(data_2d_deepcopy))} \n")

print(f"adress member 0 = {hex(id(data_2d[0]))}")
print(f"adress member 0 = {hex(id(data_2d_deepcopy[0]))}")