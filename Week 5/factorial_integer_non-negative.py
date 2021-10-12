# The program asks the user to input an integer. If the user enters a non-negative integer, 
# output the factorial of that value. If the user enters a negative integer, don't output anything

from math import factorial

value = int(input('Enter an integer >'))

if value > 0:
    factorial_of_value = factorial(value)
    print(factorial_of_value)
