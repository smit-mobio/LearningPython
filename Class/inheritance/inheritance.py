class Employee:
    company = "Google"
    
    def showDetail(self):
        print(f"The name of the company is {Employee.company}")
    
    
class programmer1(Employee):
    language = "Python"
    

class programmer2(Employee):
    language = "JS"
    company = "Youtube"
    def showDetail(self):
        print(f"The name of the company is {programmer2.company} ")    

p1 = programmer1()
p2 = programmer2()

print(p1.company)
print(p2.company)

p1.showDetail()
p2.showDetail()