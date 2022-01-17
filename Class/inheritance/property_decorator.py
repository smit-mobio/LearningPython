class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()

print(f"Total salary is {e.totalSalarxy}")