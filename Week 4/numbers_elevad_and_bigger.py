# The program asks the user to input two numbers and finds the max of those number when 
# they are raised to the power of each other. Then, display three numbers, the first number
# raised to the power of the second, the second number raised to the power of the first, and 
# then the maximum of these two computed values, each on one line

first_num = int(input('Enter an integer >'))
second_num = int(input('Enter an integer >'))

first_elev_second = pow(first_num, second_num)
second_elev_first = pow(second_num, first_num)

if(first_elev_second > second_elev_first):
    bigger_num = first_elev_second
else:
    bigger_num = second_elev_first

print(first_num, 'to the power of', second_num, 'is', first_elev_second)
print(second_num, 'to the power of', first_num, 'is', second_elev_first)
print('the max of', first_elev_second, 'and', second_elev_first, 'is', bigger_num)