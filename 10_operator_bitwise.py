a = 10
b = 5
#Bitwise OR (|)
print("==Bitwise OR==")
c = a | b
print("Nilai : ", a, ", Biary : ", format(a, "08b"))
print("Nilai : ", b, ", Biary : ", format(b, "08b"))
print("Nilai : ", c, ", Biary : ", format(c, "08b"))

#Bitwise AND (&)
print("==Bitwise AND==")
c = a & b
print("Nilai : ", a, ", Biary : ", format(a, "08b"))
print("Nilai : ", b, ", Biary : ", format(b, "08b"))
print("Nilai : ", c, ", Biary : ", format(c, "08b"))

#Bitwise XOR (^)
print("==Bitwise XOR==")
c = a ^ b
print("Nilai : ", a, ", Biary : ", format(a, "08b"))
print("Nilai : ", b, ", Biary : ", format(b, "08b"))
print("Nilai : ", c, ", Biary : ", format(c, "08b"))

#Bitwise NOT (~a)
print("==Bitwise NOT==")
b = ~a
print("Nilai : ", a, ", Biary : ", format(a, "08b"))
print("Nilai : ", b, ", Biary : ", format(b, "08b"))
 
##snifting
#snift right (>>)
print("==Bitwise Snift Right==")
a = 5
a = a >> 2
print("Nilai : ", a, ", Biary : ", format(a, "08b"))

a = 5
#snift left (<<)
print("==Bitwise Snift Left==")
a = a << 2
print("Nilai : ", a, ", Biary : ", format(a, "08b"))
