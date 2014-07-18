file = open('spell-errors.txt', 'r')

dic = {}

for line in file:
    line = line.replace('\n', '')
    lis = line.split(': ')
    correct_word = lis[0]
    wrong_words = lis[1].split(', ')
    for wrong_word in wrong_words:
        dic[wrong_word] = correct_word

file.close()
