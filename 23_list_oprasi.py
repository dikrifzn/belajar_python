data_angka = [1,2,3,1,1,3,3,4,4,5,5,2,2,4,4,5]

#count, menghitung banyak suatu data dalam list

jumlah_data_5 = data_angka.count(5)
print(f"banyak data 5 adalah {jumlah_data_5}")

#mengambil posisi data (index)
data = ["usep", "dudung", "dikrr"]
index_dudung = data.index("dudung")
print(index_dudung)

#mengurutkan data
print(f"data sebelum di sort {data_angka}")
data_angka.sort()
print(f"data setelah di sort {data_angka}")

#membalik urutan data
data_angka.reverse()
print(f"data setelah di reverse {data_angka}")