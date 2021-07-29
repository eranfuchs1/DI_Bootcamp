from anagram_checker import AnagramChecker

def menu():
    return input('(i)nsert a word or (q)uit')

def insert_word():
    word = input('insert a word: ')
    if len(word.split(' ')) > 1 or not word.strip(' ').isalpha():
        raise ValueError
    return word

if __name__ == '__main__':
    a_checker = AnagramChecker()
    choice = menu()
    if choice == 'q':
        exit()
    elif choice == 'i':
        word = insert_word()
        if a_checker.is_valid_word(word):
            print(a_checker.get_anagrams(word))
