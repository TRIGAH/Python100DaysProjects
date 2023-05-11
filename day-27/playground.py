# def add(*args):
#     sum = 0
#     for n in args:
#         sum+=n

#     print(f"The sum is {sum}")   

# add(3,3,6,5,10)      


# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiple"]
#     print(n)
# calculate(2,add=3,multiple=5)        
         
class Car:

    def __init__(self,name,**kw):
        self.name = name
        self.make = kw["make"]
        self.model = kw["model"]     

my_car = Car("Maps ",make="Nissan",model="GT-R")
print(my_car.name + my_car.model)           