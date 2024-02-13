class Fruits:
    def __init__(self,name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour
    def onyesha (self):
        print(f"My favourite fruit is {self.name} " 
              f"and it cost Ksh. {self.price }" )
myobject = Fruits("banana",40, "yellow")
myobject.onyesha()
myobject2 = Fruits("mangoes",50)
myobject2.onyesha()