##looping dari list
data_angka = [1,2,3,4,5]
data_str = ["ucup", "dudung", "dikrr", "ucup", "lulu"]
# for loop list
print("\n","="*3, "for loop", "="*3)
for angka in data_angka:
    print(f"angka = {angka}")
    
for nama in data_str:
    print(f"nama = {nama}")
    
#for loop and range
print("\n","="*3, "for loop and range", "="*3) 
panjang = len(data_angka)
for i in range(panjang):
    print(f"angka = {data_str[i]}")
    
#while loop
print("\n","="*3, "while loop", "="*3)
i = 0
panjang = len(data_angka)
while i < panjang:
    print(f"data = {data_angka[i]}")
    i+= 1
    
#list comprehension
print("\n","="*3, "list comprehension", "="*3)

data = ["ucup",1,2,3,4,"otong"]
data_angka = [1,2,3,4,5]

[print(f"data = {i}") for i in data]

data_kuadrat = [i**2 for i in data_angka]
print(f"angka kuadrat dari data_angka = {data_kuadrat}")

#enumerate
print("\n","="*3, "enumerate", "="*3)
data = ["ucup",1,2,3,4,"otong"]

for index,data in enumerate(data):
    print(f"index = {index} data = {data}")