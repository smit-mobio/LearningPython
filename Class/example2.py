class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def info(self):
        print(f"The name of the train is: {self.name}")
        print(f"Total fair of the train is: {self.fare}Rs.")
        print(f"Available seat: {self.seats}")
    
    def book(self):
        if (self.seats>0):
            print("Your ticket is booked!")
            self.seats = self.seats-1
            print(f"Remaining seats: {self.seats}")
        else:
            print("Train is full!") 
a = Train("Garibrath",300,2)
a.info()
# a.book()
# a.book() 
# a.book()
a.book()
a.book()
a.book()