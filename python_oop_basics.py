class Company:

    def __init__(self,name):
        self.name = name
        
    @staticmethod
    def add_staff(age,salary):
        print(f"addedd with age {age} and will be paid {salary}")

class Programmer(Company):
    def __init__(self, name,experience):
        super().__init__(name)
        self.experience=experience
     
    def front_end(self):
        return f"{self.name} with {self.experience} years of experience is a Frontend Developer"

    def back_end(self):
        print("Backend Developer")    

class Language(Programmer):

    def java(self):
        print(f"My name is {self.name} with {self.experience} years of experience and I do Java")

    def python(self):
        print(f"My name is {self.name} with {self.experience} years of experience and  I do Python")

    def ruby(self):
        print(f"My name is {self.name} with {self.experience} years of experience and  I do Ruby")      

c=Company("Maps") 
p=Programmer("Maps",5)
l1=Language("Ike",10)
c.add_staff(30,200)
print(l1.front_end()) 
Company.add_staff(50,400)
p.add_staff(20,500)
