# The program asks the user to input an integer. If the user enters an integer, output the negative of that integer. 
# If the user does not enter an integer, output a warning message. For this question a valid integer consists of one 
# or more digits (0-9) with an optional leading minus sign (-)

import re

string = input('Enter an integer >')

occurrences = string.count("-")
sign_remove = re.sub('-', '', string) # This method can strip multiple minus signs from the string

if string.isnumeric() == True:
    print('The negative of', string, 'is', -int(string))
elif occurrences < 2 and sign_remove.isnumeric(): # So i check that the striped string is one less than the original string
        print('The negative of', string, 'is', sign_remove)
else:
    print(string,'is not an integer')