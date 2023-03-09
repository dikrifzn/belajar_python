##LAtihan Kalkulator Sederhana

angka_pertama = float(input("Masukan Angka Pertama : "))
operator = input("Masukan Operator (+, -, x, /) : ")
angka_kedua = float(input("Masukan Angka Kedua : "))

if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"Hasil Pertambahannya adalah {hasil}")
elif operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"Hasil Pengurangannya adalah {hasil}")
elif operator == "x" or "*":
    hasil = angka_pertama * angka_kedua
    print(f"Hasil Perkaliannya adalah {hasil}")
elif operator == "/" or ":":
    hasil = angka_pertama / angka_kedua
    print(f"Hasil Pengurangannya adalah {hasil}")
else:
    print("Mohon Masukan data sesuai intruksi")
    
print("akhir dari program")