num = int(input('number between 1 and 100'))
if num % 3 == 0:
    if num % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif num % 5 == 0:
    print('FizzBuzz')
