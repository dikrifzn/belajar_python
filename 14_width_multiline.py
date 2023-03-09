#Width and Multiline

data_nama = "Dikri Fauzan Amrulloh"
data_umur = 17
data_tinggi = 165.5

#String Standar
print(5*"=" + "String Standar" + 5*"=")
data_string = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}"
print(data_string + "\n")

#String Multiline
print(5*"=" + "String Multiline" + 5*"=")
data_string = f"Nama = {data_nama}\nUmur = {data_umur}\nTinggi = {data_tinggi}"
print(data_string +"\n")

#String double three quote
print(5*"=" + "Double Three Quote" + 5*"=")
data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
"""
print(data_string + "\n")

#mengatur lebar string
print(5*"=" + "Lebar String" + 5*"=")
data_string = f"""
Nama = {data_nama :>5}
Umur = {data_umur :>5}
Tinggi = {data_tinggi :>5}
"""
print(data_string + "\n")