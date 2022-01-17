class Employee:
    company = "Google"
    salary = 5000
    def getSalary(self):
        print(f"Salary is {self.salary}")
    @staticmethod    
    def greet():
        print("Good morning, Smit!")
        
    @staticmethod
    def time():
        print(f"The time is 2pm")
smit = Employee()
vivek = Employee()
print(smit.company)
print(vivek.company)

print(smit.salary)
print(vivek.salary)

# Employee.getSalary()
smit.getSalary()
smit.greet()
Employee.greet()
Employee.time()



