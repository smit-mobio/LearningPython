class Dad:
    bcolor = "light"
    hcolor = "Brown"
    
class Mom:
    bcolor = "Fair"
    hcolor = "Black"
    bgroup = "B+"
    
class boy(Dad,Mom):
    hcolor = "light brown"
    def detail(self):
        print(f"Skin color is {self.bcolor}")
        print(f"Hair color is {self.hcolor}")
        print(f"Blood group is {self.bgroup}")
b1 = boy()
b1.detail()
