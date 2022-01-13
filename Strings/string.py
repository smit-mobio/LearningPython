a = "Hello Smit! How are you?"
print(a)
b = a[0:8]
print(b)
c= a[:10]
print(c)
d = a[0:]
print(d)
e = a[0::2]
print(e)
f = a[::-1]
print(f)

A = "smit"
A = A.capitalize()
print(A)
B = "20 is my age."
B = B.capitalize()
print(B)
# B = B.center(20)
# print(B)
B = B.center(17,"*")
print(B)

# A = A.encode()
# print(A)

A = A.endswith("m")
print(A)
A = str(A)
print(A)
x = A.count("f")
print(x)
y = A.find("s")
print(y)
z = A.index("e")
print(z)
A = A.upper()
print(A)
A = A.lower()
print(A)

A = A.replace("false","Hello Smit, Hope you are fine!")
print(A)

print(A.isalpha())
print(A.isascii())

C = "hello123"
print(C.isalnum())
print(C.isdigit())

Z = ("hello","Smit")
Z = " ".join(Z)
print(Z)