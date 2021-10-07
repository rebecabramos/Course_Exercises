# Program that prompts the user to enter two integers. 
# Then, display the result of dividing the first number by the second number, 
# using integer division so that the answer is an integer quotient, and a remainder

value1 = int(input('Enter an integer >'))
value2 = int(input('Enter an integer >'))
division = int(value1/value2)
restOfDivision = value1%value2
print(str(value1) + ' divided by ' + str(value2) + ' is ' + str(division) + ' remainder ' + str(restOfDivision))