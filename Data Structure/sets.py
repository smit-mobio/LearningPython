fruits = {"apple","banana","kiwi","oragnge","apple"}
veg = {""}
print(fruits)
print(type(veg))
set1 = {True, False,True,False}
print(set1)

set1 = {1,2,4,3,5,1}
print(set1)

for x in set1:
    print(x)
    
print(len(set1))

print("apple" in fruits)

veg.add("potato")
print(veg)
veg.pop()
print(veg)
veg2 = {"tomato","bringle","Garlic"}
veg.update(veg2)
print(veg)

veg3 = ["cucumber",'walnut']
veg.update(veg3)
print(veg)

veg.remove("cucumber")
# veg.remove("cucumber")
print(veg)

veg.discard("cucumber")
print(veg)
# veg = tuple(veg)

# del fruits
# print(fruits)

set2 = {1,5,10,4}

print(set1)
print(set2)

set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set1.intersection_update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
