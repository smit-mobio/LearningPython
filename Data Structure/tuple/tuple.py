x = (1,5,8,9,True)
print(x)

# x[1]="smit"
# print(x)

y = ("Smit",)
print(y)

print(x[:4])

if 5 in x:
    print("yes")
else:
    print("no")
    
x +=(8,10)
print(x)

X = x.index(8)
print(X)

X = x.count(8)
print(X)

print(len(x))

thistuple = ("apple", "banana", "cherry")
thistuple = list(thistuple)
print(thistuple)
thistuple.remove("apple")
print(thistuple)
thistuple = tuple(thistuple)
thistuple += (1,2)
print(thistuple)
# del thistuple
# print(thistuple)
thistuple += ("mango","guava")
a,b,*c = thistuple
print(a)
print(b)
print(*c)
print(thistuple)
a,*b,c = thistuple
print(a)
print(*b)
print(c)

for x in thistuple:
    print(x)
    
for i in range(len(thistuple)):
    print(thistuple[i])
    
print(thistuple)

i = 1
while i < len(thistuple):
    print(thistuple[i])
    i= i+1
    
fruits = ("apple","mango","cherry","graps")
veg = ("tomato","potato")
veg = veg*2
print(fruits+veg)
print(veg)