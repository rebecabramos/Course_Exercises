# The program that creates an empty list and an empty tuple, 
# then asks the user for an input string 
# and adds it to the tuple and empty list

print('[]')
print('()')

# user input
my_string = input('Enter a string >')

# create tupla and list empty
my_tuple = ()
my_list = []

# from tuple to the new list for easy addition to the empty tuple
l = list(my_tuple)
l.append(my_string)

# adding element to list
my_list = [my_string]

# tuple function creates a new tuple whose elements are the same 
# as the argument object, which in this case is your list containing the str object
# list is multable, tuple not!
my_tuple = tuple(l)

# show tuple and list
print(my_list)
print(my_tuple)
