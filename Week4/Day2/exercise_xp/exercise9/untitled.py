fruits = input('enter your favorite fruits (space delimited): ').split(' ')
if input('enter a fruit name: ') in fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')
