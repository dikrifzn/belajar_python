# tingkat = 10
# count = 1
# for i in range(tingkat):
#     print("*"*count)
#     count += 1

# i = 1
# while i < tingkat:
#     print("*"*i)
#     i += 1
        
# spasi = tingkat * 2 +1 #5 * 2 + 1 = 11
# bintang = 1
# while spasi > 0:
#     print(" "*bintang, "*"*spasi)
#     spasi -= 2
#     bintang += 1

###Ketupat
# tingkat = int(input("Masukan tingkat segitiga : "))
# bintang = 1
# spasi = tingkat
# while bintang <= tingkat:
#     print(" "*spasi, "*"*bintang)
#     bintang += 2
#     spasi -= 1
#     if bintang > tingkat:
#         # bintang -= 2
#         # spasi += 1
#         while bintang > 0:
#             bintang -= 2
#             spasi += 1
#             print(" "*spasi, "*"*bintang)
#         else:
#             break
        
#I am so strugling when built this code XO

###love

bintang = 24
spasi = 1
print(" "*4, "*"*6, " "*4, "*"*6)
print(" "*2, "*"*9, " "*2, "*"*9)
print(" ","*"*bintang)
while bintang >= 0:
    print(" "*spasi, "*"*bintang)
    bintang -= 4
    spasi += 2