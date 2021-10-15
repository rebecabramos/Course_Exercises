# The program performs space-separated string conversion in a list
# and then cycles through each index of the list 
# and displays the result in capital and capital letters

string = input('Enter some words >')

list_string = string.split()
print(list_string)

for x in list_string:
    print(x, x.upper())
