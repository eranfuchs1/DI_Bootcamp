def letters_count(word):
    answer = {}
    for l in word:
        if l in answer:
            answer[l] += 1
        else:
            answer[l] = 1
    return answer

class AnagramChecker:
    def __init__(self, fname='sowpods.txt'):
        with open(fname, 'r') as f:
            self.__load_words(f)
    def __load_words(self, f):
        self.words = list(map(lambda w: w.rstrip('\n').lower(), f.readlines()))
    def is_valid_word(self, word):
        return word in self.words
    def get_anagrams(self, word):
        return list(filter(lambda w: set(w) == set(word) and w != word and letters_count(w) == letters_count(word), self.words))
