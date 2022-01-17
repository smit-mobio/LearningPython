class Employee:
    company = "Google"
    salary = 5000
smit = Employee()
vivek = Employee()
print(smit.company)
print(vivek.company)

print(smit.salary)
print(vivek.salary)

smit.salary = Employee.salary + 1000
vivek.salary = 8000
print(smit.salary)
print(vivek.salary) 