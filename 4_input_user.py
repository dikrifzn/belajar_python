#mengambil inputan yang di masukan user
data_user = input("Masukan Sesuatu : ")
print("tipe data ", data_user, "Adalah ", type(data_user)) #data yang dimasukan pasti string

#mendapatkan input integer dari user
data_int_user = int(input("Masukan angka : "))
print("tipe data ", data_int_user, "Adalah ", type(data_int_user))

#mendapatkan input boolean dari user
data_bool_user = bool(int(input("Masukan 1 untuk true dan 0 untuk false : ")))
print("tipe data ", data_bool_user, "Adalah ", type(data_bool_user))
