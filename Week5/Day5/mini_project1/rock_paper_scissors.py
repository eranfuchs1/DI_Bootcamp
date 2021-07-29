from game import Game
def get_user_menu_choice():
    return input('(p)lay a new game, (s)how scores or (q)uit: ')

def print_results(results):
    print(results)

def keep_results(g):
    global results
    results['draws'] += g.result == 'draw'
    results['wins'] += g.result == 'user'
    results['losses'] += g.result == 'computer'

def main():
    while True:
        choice = get_user_menu_choice()
        if choice == 'q':
            break
        elif choice == 'p':
            keep_results(Game().play())

        elif choice == 's':
            print_results(results)

results = {'draws':0,'wins':0,'losses':0}

if __name__ == '__main__':
    main()
