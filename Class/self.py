class Employee:
    company = "Google"
    salary = 5000
    def getSalary(self):
        print(f"Salary is {Employee.salary}")
smit = Employee()
vivek = Employee()
print(smit.company)
print(vivek.company)

print(smit.salary)
print(vivek.salary)

# Employee.getSalary()
smit.getSalary()


