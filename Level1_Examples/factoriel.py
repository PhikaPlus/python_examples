number = int(input('enter a positive integer number: '))
fact = number

while number > 1:
    fact = fact * (number - 1)
    number = number - 1


print('{}!:\t{}'.format(number, fact))

# ----------------------------------- 2 --------------------------------
from math import factorial
print (factorial(number))
