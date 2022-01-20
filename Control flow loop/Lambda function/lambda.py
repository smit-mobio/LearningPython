x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))