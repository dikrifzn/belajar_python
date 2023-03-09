##LIst adalah kumpulan berbagai data

data_angka = [1,2,3,4,5,]
print(data_angka)

data_str = ["otong", "ucup", "dikrr"]
print(data_str)

data_bool = [True, False, True, True]
print(data_bool)

data_campur = [1, "ucup", True, "otong", False]
print(data_campur)

#cara alternatif membuat list
data_range = range(1,10)
data_list_range = list(range(1,10))
data_list_range2 = list(range(1,10, 2))

print(data_range)
print(data_list_range)
print(data_list_range2)

#membuat list dengan for
list_for = [i for i in range(0,10)]
list_for2 = [i**2 for i in range(0,10)]
print(list_for)
print(list_for2)

#list for if
list_if = [i for i in range(0,10) if i != 5]
print(list_if)

#mengambil data dari list
#index     0        1       2
data = ["dikri", "ucup", "otong"]
print(f"data pertama index pertama = {data[0]}")

print(f"data pertama index terakhir = {data[-1]}")

panjang_data = len(data)
print(f"pajang data = {panjang_data}")

##Maniulsi data list
print(f"data sebelum di ubah {data}")

#menambah data sesuai posisi
data.insert(1, "tambahan")
print(data)

#menambahkan data di akhir
data.append("akhiran")
print(data)

#menggabung data list
data_2 = list(range(0,5))
data.extend(data_2)
print(data)

#merubah data list
data[2] = "usep"
print(data)

#meremove data list
data.remove("usep")
print(data)

#meremove data paling belakang
data.pop()
print(data)