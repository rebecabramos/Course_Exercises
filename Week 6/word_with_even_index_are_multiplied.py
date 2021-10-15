# The program that enters the user's words, one per line, and saves the words in a list until 
# the user enters the word (stop). The word stop must not be included in the list. The program must
# then generate the list. It must then replace each word that has an even index in the word list, 
# by the word length multiplied by the index. It must then generate this modified list

word_list = []
new_list = []
word = input('Enter a word >')

while word != 'stop':
    word_list.append(word)
    word = input('Enter a word >')
print(word_list)

for index in range(0, len(word_list)):
    if index%2 != 0:
        new_list.append(word_list[index])
    else:
        multiplication = index*len(word_list[index])
        new_list.append(multiplication)
print(new_list)