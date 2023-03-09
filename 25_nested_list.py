##nested list (list bersarang)

data_0 = [1,2]
data_1 = [3,4]

data_a = [data_0, data_1]
print(f"data a = {data_a}")

peserta_1 = ["dikri", 19, "kuningan"]
peserta_2 = ["ujang", 20, "merauke"]
peserta_3 = ["malika", 17, "sumedang"]

peserta_lomba = [peserta_1, peserta_2, peserta_3]
print(f"peserta lomba = {peserta_lomba}")

for peserta in peserta_lomba:
    print(f"nama : {peserta[0]}")
    print(f"umur : {peserta[1]}")
    print(f"alamat : {peserta[2]} \n")