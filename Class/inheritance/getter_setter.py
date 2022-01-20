class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    

    
    def get_totalSalary(self):
        return self.salary + self.salarybonus
    
    def set_totalsalary(self,s,y):
        self.salarybonus = s
        self.salary = y

e = Employee()
print(e.get_totalSalary())
e.set_totalsalary(200,5000)
print(e.get_totalSalary())

# class Javatpoint:  
#    def __init__(self, age=49):  
#       self._age = age  
# # make the getter method  
#    def get_age(self):  
#       return self.__age  
# # make the setter method  
#    def set_age(self, a):  
#       self.__age = a  
# grad_obj = Javatpoint()  
# print(grad_obj._age)  
# # grad_obj.set_age(50)
# # print(grad_obj.get_age())
# # Before using setter  
# # print(grad_obj.get_age())  
# # # After using setter  
# grad_obj.set_age(2020)  
# print(grad_obj.get_age())  