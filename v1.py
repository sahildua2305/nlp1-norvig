import re, collections

words = re.findall('[a-z]+', open('big.txt').read().lower())

file = open('spell-errors.txt', 'r')

model = collections.defaultdict(lambda: 0)

for line in file:
    line = line.replace('\n', '')
    lis = line.split(': ')
    correct_word = lis[0]
    wrong_words = lis[1].split(', ')
    for wrong_word in wrong_words:
        model[wrong_word] = correct_word

file.close()

while(1):
    w = raw_input()
    if w=='': break
    if w in words or model[w] == 0:
        print w
    else:
        print model[w]
