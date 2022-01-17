class Calculator:
    def __init__(self, num):
        self.num = num
    
    def sqaure(self):
        print(f"Sqaure of {self.num} is: {self.num**2} ")
    
    def cube(self):
        print(f"Cube of {self.num} is: {self.num**3}")
        
    def squareRoot(self):
        print(f"Sqaureroot of {self.num} is: {self.num**(1/2)}")
sqaure = Calculator(10)
cube = Calculator(4)
squareroot = Calculator(25)
sqaure.sqaure()
cube.cube()
squareroot.squareRoot()