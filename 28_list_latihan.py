#latihan data perpustakaan
kumpulan_data_buku = []
while True:
    judul_buku = input("Judul Buku\t: ")
    penulis_buku = input("Penulis\t\t: ")

    data_buku = [judul_buku, penulis_buku]

    kumpulan_data_buku.append(data_buku)
    print("|\tNo\t|\t\tJudul\t\t|\tPenulis\t\t|")
    for index,buku in enumerate(kumpulan_data_buku):
        print(f"|\t{index+1}\t|\t\t{buku[0]}\t\t|\t{buku[1]}\t\t|")
    if input("apakah ingin menambahkan lagi?(y/n) : ") == "n":
        break
print("akhir dari program")