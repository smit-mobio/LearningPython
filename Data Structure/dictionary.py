thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year" :2001
}

print(thisdict)
print(thisdict["brand"])

car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(car["colors"])

print(len(car))
print(type(car))

print(car.values())
print(car.keys())

car["year"] = 2022
print(car)

x = car["year"]
print(x)

y = car.keys()
print(y)

print(car.items())

print(car.get("year"))

print(car)

print("brand" in car)

if "model" in car:
    print("yes")
else:
    print(None)
    
print(car)

car.update({"electric":True})
car["electric"] = False
print(car)

car["model"] = "mustang"
print(car)

car.update({"price":"20000000"})
print(car)

car.pop("price")
print(car)

car.popitem()
print(car)

# del car
# print(car)

del car["year"]
print(car)

# car.clear()
# print(car)

for x in car:
    print(car[x])
    
for x in car:
    print(x)
    
for x in car.keys():
    print(x)
    
for x in car.values():
    print(x)

for x,y in car.items():
    print(x,y)
    
car1 = car.copy()
print(car1)

car2 = dict(car)
print(car2)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

a = [1,2,5]
print(sum(a))