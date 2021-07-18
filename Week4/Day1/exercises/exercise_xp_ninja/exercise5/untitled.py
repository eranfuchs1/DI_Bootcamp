size = 0
sentence = ''
while True:
    sentence = input('enter the longest sentence you can without the letter \'a\' or \'A\'')
    if 'a' in sentence.lower():
        continue
    if len(sentence) > size:
        print('congrats')
        size = len(sentence)
