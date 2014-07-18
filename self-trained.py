import re, collections

file = open('spell-errors.txt', 'r')
model1 = collections.defaultdict(lambda: 0)
for line in file:
    line = line.replace('\n', '')
    lis = line.split(': ')
    if len(lis) > 1:
        correct_word = lis[0]
        wrong_words = lis[1].split(', ')
        for wrong_word in wrong_words:
            model1[wrong_word] = correct_word
file.close()

tokens = re.findall('[a-z]+', open('big.txt').read().lower())
def train(tokens):
    model2 = collections.defaultdict(lambda: 1)
    for t in tokens:
        model2[t] += 1
    return model2

nwords = train(tokens)
alphabet= 'abcdefghijklmnopqrstuvwxyz'
def edits1(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word)+1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known(words):
    return set(w for w in words if w in nwords)

while(1):
    w = raw_input()
    if w=='': break
    if model1[w] != 0:
        correct_word = model1[w]
        print correct_word,
    else:
        options = known([w]) or known(edits1(w)) or [w]
        correct_word = max(options, key=nwords.get)
        print correct_word,
    if correct_word != w:
        print "\nDo you want to use our corrected word? (y/n): ",
        response = raw_input()
        if response == 'y':
            with open("spell-errors.txt", "a") as myfile:
                myfile.write('\n' + correct_word + ': ' + w)
        elif response == 'n':
            print "\nPropose your word for future reference: ",
            r = raw_input()
            if len(r)>1:
                with open("spell-errors.txt", "a") as myfile:
                    myfile.write('\n' + r + ': ' + w)
    else:
        print
