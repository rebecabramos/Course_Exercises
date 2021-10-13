# The program create a list containing the integers from (1 to 10) in increasing order, and outputs the list. 
# Then prompt the user to enter a number between 1 and 10, replace this number by the str object (gone) and output the list.
# If the user enters a string that does not  represent an integer between 1 and 10, instead output the appropriate message

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sequence)

number_for_verification = input('Enter an integer between 1 and 10 >')

for x in sequence:
    if number_for_verification.isnumeric() == True:
      if int(number_for_verification) >= sequence[0] and int(number_for_verification) <= sequence[-1]:
        if x == int(number_for_verification):
            # knowing that the list in python starts with index zero, 
            # so the third element corresponds to position two of the list
            sequence[x-1] = 'gone' 
            print(sequence)
            break
      else:
        print(number_for_verification, 'is not between 1 and 10')
        break
    else:
        print(number_for_verification, 'is not a positive integer')
        break