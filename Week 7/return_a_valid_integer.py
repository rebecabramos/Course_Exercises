import re

def as_integer(an_object):

    is_interger_list = []

    for x in range(len(an_object)):
        if type(an_object[x]) == str: # check if the string is valid
            if str(an_object[x]).count("-") == True: # if the valid string starts with (-) or has
                sign_remove = re.sub('-', '', an_object[x]) # that character is stripped
                if str(sign_remove).isnumeric() == True: # then check if this string with (-) is a number
                    is_interger_list.append(an_object[x])
                else:
                    is_interger_list.append("None")
            if str(an_object[x]).isnumeric() == True: # then check if this string is a number
                is_interger_list.append(an_object[x])
        else:
            is_interger_list.append("None")
        
    return is_interger_list
  
def main():
    element_list = []

    element = input()

    element_list.append(element)

    verified_integer_list = as_integer(element_list)
    
    for x in range(len(verified_integer_list)):
        print(verified_integer_list[x])

main()