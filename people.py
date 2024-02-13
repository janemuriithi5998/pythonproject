class People:
    def __init__(self,name, age,):
        self.name = name
        self.age =age
    def onyesha(self):
        print(f"my name is {self.name} " f"and  I am {self.age}")
myobject = People("Portia", 23)
myobject1 = People("Philip", 25)
myobject2 = People("Lenis", 20)
myobject3 = People("Joseph", 26)
myobject4 = People("Frank", 28)
myobject.onyesha()
myobject1.onyesha()
myobject2.onyesha()
myobject3.onyesha()
myobject4.onyesha()