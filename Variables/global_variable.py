x = "Smit"
def name():
    print(f"My name is {x}")
    
name()


def name1():
    x = "Meet"
    print(f"My name is {x}")
    
name1()
print(f"My name is {x}")

def name2():
    global x
    x = "Hiren"
    
name2()
print(f"My name is {x}")
