import random
import datetime as dt
import calendar

# x = random.randint(1,20)

# if x%2 == 0:
#     print("HEAD")
# else:
#     print("TAIL")    

from re import A


a=2
b=10
i=0

while i < 4:
    a+=a 
    i+=1 
print(a)   
print(i) 


def addMonths(inpDt, mnths):
  tmpMnth = inpDt.month - 1 + mnths

  # Add floor((input month - 1 + k)/12) to input year component to get result year component
  resYr = inpDt.year + tmpMnth // 12

  # Result month component would be (input month - 1 + k)%12 + 1
  resMnth = tmpMnth % 12 + 1

  # Result day component would be minimum of input date component and max date of the result month (For example we cant have day component as 30 in February month)
  # Maximum date in a month can be found using the calendar module monthrange function as shown below
  resDay = min(inpDt.day, calendar.monthrange(resYr,resMnth)[1])

  # construct result datetime with the components derived above
  resDt = dt.datetime(resYr, resMnth, resDay, inpDt.hour, inpDt.minute, inpDt.second, inpDt.microsecond)

  return resDt

# let's test our function with current time
nowDt = dt.datetime.now()

print('Now =', end=' ')
print(nowDt)

print('Now + 2 months =', end=' ')

duration = 3
i=1
while i <= duration:
  print(addMonths(nowDt, i))
  i+=1
