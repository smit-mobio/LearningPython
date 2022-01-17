class Employee:
    company = "Google"
    salary = 5000
    
    def __init__(self,name,unit):
        self.name = name
        print(f"Hello sir! Your name is {name} and you are working with {unit}")
    def getDetails(self):
        print(f"Your name is {self.name}")    
    @staticmethod    
    def greet():
        print("Good morning, Smit!")
        
    @staticmethod
    def time():
        print(f"The time is 2pm")
smit = Employee("Smit","Xbox")
# vivek = Employee() -> This throws an error: (missing 2 required positional arguments: 'name' and 'unit')
smit.getDetails()




