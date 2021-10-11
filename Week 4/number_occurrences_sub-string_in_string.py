# The program that asks the user to input a string and a sub-string 
# and outputs the number of occurrences of the sub-string in the string

my_string = input("Enter a string >")
my_substring = input("Enter a substring >")

occurrences = my_string.count(my_substring)

result = "the substring \"" + my_substring + "\" appears " + str(occurrences) + " times in \"" + my_string + "\""

print(result)