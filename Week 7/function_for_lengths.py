# The program used functions for display an list of words and list of lenghs 

def string_lengths(string_list):
    # The string_lengths function which must output the original list and 
    # the list of lengths of words in the original list
    
    length_list = []

    for x in string_list:
        length_list.append(len(x))

    print(string_list)
    print(length_list)

def main():
    # The main function must input a string, split it into a list of words 
    # and call the string_lengths function

    string = input('Enter some words >')

    string_list = string.split()
    string_lengths(string_list)

main()