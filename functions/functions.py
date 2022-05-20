# def greet_with(name,location):
#     print(f'Hello {name}')
#     print(f'What is it like in {location}')

# greet_with(location='lokogoma',name='Olu')    

# Coding Exercise for Paint Calculator
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# def paint_calc(height,width,cover):
#     result= (test_h * test_w)/coverage
#     result_round=round(result)
#     print(f'You will need {result_round} cans of paint. ')

# paint_calc(height=test_h, width=test_w, cover=coverage)

# Coding Exercise of Prime Number Checker

# Note:- Always think of more than one way to solve a problem
def prime_checker(number):
    is_prime=True
    for x in range(2,number):
        if number%x == 0:
            is_prime=False
    if is_prime:        
       print('It\'s a prime number')

    else:
       print('it\'s not a prime number')        
      
n=int(input('Check this number: '))
prime_checker(number=n)