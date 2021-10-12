# The program asks the user to input a non-negative integer. 
# If the user enters a non-negative integer, output two times that value. 
# If the user does not enter a non-negative integer, output a warning message

value = input('Enter a non-negative integer >')

if value.isnumeric() == True:
    multiplication = int(value)*2
    print(value, '* 2 is', multiplication)
else:
    print( value,'is not a non-negative integer')