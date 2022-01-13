import colorsys


veg = ["tomato", "potato","salads","carrot"]

for x in veg:
    print(x)

for x in range(1,len(veg)):
    print(veg[x])
    
name = "Vivek"
for x in name:
    print(x)

for x in veg:
    print(x)
    if x == "potato":
        break
    
for x in veg:
    if x == "salads":
        break
    print(x)
    
for x in veg:
    if x == "salads":
        continue
    print(x)

x = 0
for x in range(6):
    print(x)
    
for x in range(2,6):
    print(x)

for x in range(2,11,2):
    print(x)
    
for x in range(6):
    print(x)
else:
    print("finally done!")

for x in range(6):
    if x == 4:
        break
    print(x)
else:
    print("Finally!")
    
colors = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    for y in colors:
        print(y,x)
        
for x in fruits:
    for y in colors:
        print(x,y)
