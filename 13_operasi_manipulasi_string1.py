#Menyambung string
nama_pertama = "Dikri"
nama_tengah = "Fauzan"
nama_akhir = "Amrulloh"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

#Menghitung Panjang String
panjang = len(nama_lengkap)
print("Panjang dari : " + nama_lengkap + " = ", panjang)

##operator untuk string
##mengecek apakah ada komponen char atau string di string

d = "D"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

e = "E"
status = e not in nama_lengkap
print(e + " Tidak ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("wk"*10)
print(15*"wk")

#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-7) : " + nama_lengkap[-7])
print("index ke-(0-4) : " + nama_lengkap[0:5])

#item paling kecil
print("Paling kecil : " + min(nama_lengkap))
print("Paling Besar : " + max(nama_lengkap))

#operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))