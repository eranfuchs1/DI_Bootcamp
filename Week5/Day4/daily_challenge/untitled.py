class Text:
    def __init__(self, text):
        self.text = text
    def __word_freq(self, word):
        return len(list(filter(lambda w: w == word, self.text.split(' '))))
    def word_freq(self, word):
        freq = self.__word_freq(word)
        return f'{word} appears {freq} in the text' if freq else None
    def __dict__(self):
        d = {}
        for w in self.text.split(' '):
            d[w] = d[w] + 1 if w in d else 1
        return d
    def __list__(self):
        return list(dict(self).keys())
    def most_common_word(self):
        word = None
        count = 0
        for k, v in dict(self):
            if count < v:
                word = k
                count = v
        return word
    def unique_words(self):
        return list(self)
    @classmethod
    def from_file(cls, fname):
        with open(fname, 'r') as f:
            return cls(f.read())

class Str(str):
    def remove_list(self, arr):
        return Str(self.replace(arr[0], '')).remove_list(arr[1:]) if len(arr) > 1 else self.replace(arr[0], '')

class TextModification(Text):
    def no_punctuation(self):
        return Str(self.text).remove_list(list(',.\'";()[]{}'))
    def no_stopwords(self):
        return Str(self.text).remove_list(list(Text.from_file('stopwords.txt').text))
    def no_specialchars(self):
        return Str(self.text).remove_list(list(' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\'"'))


print(TextModification.from_file('the_stranger.txt').no_stopwords())
print(TextModification.from_file('the_stranger.txt').no_specialchars())
print(TextModification.from_file('the_stranger.txt').no_punctuation())
