# Company,Programmer,Language

class Company:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def add_staff(age,salary):  
        print(f"A staff  with {age} and salary {salary} dollars")  

class Programmer(Company):
    def __init__(self,name,experience):
        super().__init__(name)
        self.experience=experience

    def front_end(self):
        print(f"{self.name} with {self.experience} years of experience is a front-end developer.")    

    def back_end(self):
        print(f"{self.name} with {self.experience} years of experience is a back-end developer.")    

class Language(Programmer):

    def java(self):
        print(f"{self.name} is good in Java")

    def go(self):
        print(f"{self.name} is not good in GO")            



# c=Company("Maps")    
# p=Programmer("Julius",4)
# l=Language("Obi",7)
# p.front_end()
# p.back_end()   
# l.go()   

# Label,Artist,Genre

class Label:
    def __init__(self,name,slogan):
        self.name=name
        self.slogan=slogan

    @staticmethod
    def add_talent(age,worth):
        print(f"A talent was added with age {age} and worths {worth} million dollars")   


class Artist(Label):
    def __init__(self, name, slogan,level):
        super().__init__(name, slogan)         
        self.level=level

    def solo(self):
        print(f"{self.name} with slogan {self.slogan} is a Solo Artist at level {self.level} ")    

    def band(self):
        print(f"{self.name} with slogan {self.slogan} is a Band at level {self.level} ")    

class Genre(Artist):

    def rnb(self):
        print(f"{self.name} with slogan {self.slogan} is not an RnB Artist")

    def afropop(self):
        print(f"{self.name} with slogan {self.slogan} is an Afropop Artist")


l=Label("Mavin","Ait")    
a=Artist("Jonzin","coko",4)
g=Genre("Maps","mapam",5)
g.afropop()
g.solo()
a.band()
l.add_talent(20,5000)    