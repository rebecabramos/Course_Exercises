def as_integer(an_object):
    
    is_interger_list = []

    for x in an_object:
        print(x)
        if x.isnumeric() == True:
            number = x
            print(number)
            is_interger_list.append(number)
        else:
            is_interger_list.append("None")

    return is_interger_list
  
def main():
    element_list = []

    element = input()

    element_list.append(element)
    result_list = as_integer(element_list)

    for x in result_list:
        print(x)

main()