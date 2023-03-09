#Date and Time

import datetime

hari_ini = datetime.date.today()
print(hari_ini)
print(f"hari ini adalah hari {hari_ini:%A}")

tanggal = datetime.date(2003, 11, 23)
print(tanggal)
print(f"Hari ini adalah hari {tanggal:%A}")

user_tanggal = int(input("Masukan Tanggal lahir : "))
user_bulan = int(input("Masukan Bulan Lahir : "))
user_tahun = int(input("Masukan Tahun Lahir : "))
user_lahir = datetime.date(user_tahun, user_bulan, user_tanggal)

print(f"Hari saat anda lahir ialah hari {user_lahir:%A}")
hari_ini = datetime.date.today()
user_umur = hari_ini - user_lahir
user_umur = user_umur.days // 365
print(f"Umur anda saat ini adalah {user_umur} tahun")