#Latihan Konversi Satuan Temperature
judul = "Konversi Suhu"
judul = judul.upper()
print(judul, "\n")

##Celcius ke satuan suhu lain
celcius = float(input("Masukan suhu (celcius) : "))

#Reamur
reamur = (4/5)*celcius
print("Reamur = ", reamur)

#Fahrenheit
fahrenheit = ((9/5)*celcius)+32
print("Fahrenheit = ", fahrenheit)

#Kelvin
kelvin = celcius + 173
print("Kelvin = ", kelvin)

##Reamur ke satuan suhu lain
reamur = float(input("Masukan suhu (reamur) : "))

#celcius
celcius = (5/4)*reamur
print("Celcius = ", celcius)

#Fahrenheit
fahrenheit = ((9/4)*reamur)+32
print("Fahrenheit = ", fahrenheit)

#Kelvin
kelvin = ((5/4)*reamur)+273
print("Kelvin = ", kelvin)


##Fahrenheit ke satuan suhu lain
reamur = float(input("Masukan suhu (fahrenheit) : "))

#celcius
celcius = (5/9)*(fahrenheit-32)
print("Celcius = ", celcius)

#Reamur
reamur = (4/9)*(fahrenheit-32)
print("Reamur = ", reamur)

#Kelvin
kelvin = (5/9*(fahrenheit-32))+273
print("Kelvin = ", kelvin)


##Kelvin ke satuan suhu lain
kelvin = float(input("Masukan suhu (kelvin) : "))

#celcius
celcius = kelvin - 273
print("Celcius = ", celcius)

#Reamur
reamur = (4/5)*(kelvin-32)
print("Reamur = ", reamur)

#Fahrenheit
fahrenheit = (1.8*(kelvin-273))+32
print("fahrenheit = ", fahrenheit)