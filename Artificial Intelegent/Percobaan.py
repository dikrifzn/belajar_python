#untuk membuat file baru
buatFile = open("/home/netwreck/Documents/Website Developer/A.I/fileBaru.py", "w")

#untuk menambahkan syntax kedalam file baru
buatFile.write("print('hello!')" + "\n")
buatFile.write("print('apakabar?')" + "\n")

buatFile.write(
"""
x = 1
y = 4
z = x + y
print(z)
"""
)
#untuk menutup file
buatFile.close