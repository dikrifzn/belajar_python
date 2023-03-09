salam = "bro!"
print("normal = " + salam)

#merubah string ke uppercase
salam = salam.upper()
print("upper = " + salam)

#merubah string ke lowercase
alay = "aKu KeCe AbiezzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

#pengecekan dengan isX method
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_lower = salam.isupper() #hasilnya bool
print(salam + " is upper = " + str(apakah_lower))

#penggabungan komponen join() split()
pisah = ["satu", "dua", "tiga"]
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = " iya ".join(pisah)
print(gabung)

gabung = gabung.split(" ")
print(gabung)

#alokasi karakter rjust() ljust() center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

center = "center".center(10)
print("'"+center+"'")

center = "center".center(15, "=")
print("'"+center+"'")

#penghapus character
blabla = "ada tanda :"
print(blabla)
blabla = blabla.strip(":") #menghilangkan tanda :
print(blabla)
