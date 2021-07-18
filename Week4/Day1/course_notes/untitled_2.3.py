num = int(input('number between 1 and 100'))
if num % 3 == 0 or num % 5 == 0:
    if num % 3:
        print('Buzz')
    elif num % 5:
        print('Fizz')
    else:
        print('FizzBuzz')
