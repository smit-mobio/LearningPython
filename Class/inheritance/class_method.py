class Fruits:
    name = "Apple"
    color = "Red"
    @classmethod
    def changeColor(cls,clr):
        cls.color = clr
        # cls.color = color
        
f = Fruits()
print(f.color)
f.changeColor("Yellow")
print(f.color)