# The program that asks the user to input a string that has an (e) as the middle character. 
# If the string has an odd number of characters and an (e) as the middle character, output a positive message. 
# If the string has an even number of characters or has an odd number and the middle character is not an (e), 
# output a negative message

string = input('Enter a string with an e in the middle >')
position = 0
middle = (len(string)-1)/2 

for n in string:
    if len(string)%2 == 0:
      print('No,', string, 'has no middle character')
      break
    else:
      if position == middle:
        if n == 'e':
          print('Yes,', string, 'has', n, 'in the middle, at index', position)
          break
        else:
          print('No,', string, 'has', n, 'in the middle, at index', position)
          break
    position += 1
