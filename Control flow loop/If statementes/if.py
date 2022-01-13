from tkinter.messagebox import NO


a = 10 
b = 50

print(f"a : {a}")
print(f"b : {b}")

if a < b:
    print("a is less than b!")
else:
    print(None)
    
if a > b:
    print("a is greater than b!")
elif a > 5 and a < 11:
    print("a is greater than 5 and less than 11!")
else:
    print(None)
    
x = 40
y = 40

print("x : 40")
print("y : 40")
if x > y:
    print("x is greater than y")
elif x==y:
    print("Both are equal!")
    
x = 40
y = 45

print("x : 40")
print("y : 45")

if x > y:
    print("x is greater than y")
elif x==y:
    print("Both are equal!")
else:
    print("y is greater than x")
    

A = 85
B = 85

print(f"\nA : {A}")
print(f"B : {B}")
if A >= B : print("\nA is greater than B\n")

X = 100
Y = 200

print(f"{X}") if X > Y else print(f"X = Y") if X == Y else print(f"{Y}")

a = 20
b = 3
c = 400

if a > b and b < c:
  print(f"a : {a}, b : {b},c : {c}")
  
a = 200
b = 33
c = 500

if a > b or a > c:
  print("At least one of the conditions is True")
  
x = 50

if x > 10:
    if x > 50:
        print(f"x is greater than {x}")
    else:
        print(f"x is less than or equal to 50")
        
a = 500
b = 200

if a > b:
    pass