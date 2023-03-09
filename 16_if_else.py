#IF and ELSE Statment

## IF Inline 
# if kondisi: aksi
# program selanjutnya

nama = input("Masukan Nama : ")
# if nama == "ucup": print("Hallo Ucup!")
# print(f"Terimakasih {nama}")

## IF Indentation
# if kondisi:
#     aksi
# program selanjutya

# if nama == "ucup":
#     print("Hai Ucup !")
# print(f"Terimakasih {nama}")

##ELSE Statement
# if nama == "ucup":
#     print("Hai Ucup! Kamu Keren!")
# else:
#     print("Kamu bukan Ucup! Kamu Gak Keren!")
# print("akhir dari program")

##ELIF statement
if nama == "ucup": #kondisi true 1
    print("Selamat Datang Manager!")
elif nama == "otong": #kondisi true 2
    print("Selamat Datang Asistant Manager!")
elif nama == "udin": #kondisi true 3
    print("Selamat Datan Karyawan!")
else: #kondisi false
    print("Anda Bukan Bagian Dari Perusahaan!")
    
print("akhir dari program")