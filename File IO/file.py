import os
f = open("fruits.txt","r")
r = f.read()
po = f.tell()
print(po)
print(r)
f.close()

os.rename("fruits.txt","Fruits.txt")

os.remove("abs.txt") 