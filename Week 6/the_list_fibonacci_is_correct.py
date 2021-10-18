# The program prompt the user to enter the Fibonacci numbers in order, starting at 1, 
# until the user either makes a mistake or enters the first Fibonacci number greater than 50. 
# If the user makes an error, output a consolation message. If the user enters all of the 
# Fibonacci numbers successfully then output a congratulations message

previous_number = 0
sum_inputs = 1
my_list = []
list_fibonacci = [1,1,2,3,5,8,13,21,34,55]

current_number = int(input('Enter the next Fibonacci number >'))
my_list.append(current_number)

while current_number < 50:
    previous_number = current_number
    current_number = int(input('Enter the next Fibonacci number >'))

    sum_inputs += previous_number

    if current_number != sum_inputs-previous_number:
        print('Try again')
        break

    my_list.append(current_number)

if my_list == list_fibonacci:
    print('Well done')