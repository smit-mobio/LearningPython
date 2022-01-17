try:
    print("trying to execute 1/0")
    print(1/0)
except:
    print("Threw an error")
finally:
    print("Final clause!")
    

try:
    print(x)
except NameError:
    print("NameError occured")
except:
    print("Something went wrong")
    
try:
    print("Hello Smit!")
except:
    print("Something went wrong")
else:
    print("No error occured")