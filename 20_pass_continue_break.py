##pass, continue, dan break

#pass
print("="*5 + "PASS")
angka = 0
while angka < 5:
    angka += 1
    print(angka)
    if angka == 3:
        print("TIGA")
        pass #Tidak akan di esekusi (hanya pengisi)

print("akhir dari program \n")

#continue
print("="*5 + "CONTINUE")
angka = 0
while angka < 5:
    angka += 1
    print("angka sekarang", angka)
    if angka == 3:
        print("TIGA!!")
        continue #menskip step selanjutnya
    print("SKIP!")
    print("SKIP2!")
print("akhir dari program \n")

#break
print("="*5 + "BREAK")
angka = 0
while angka < 5:
    angka += 1
    print("angka sekarang", angka)
    if angka == 3:
        print("Betool")
        break #menghentikan looping
    print("Lanjoot!")
print("akhir dari program")