factorial = lambda num: num * factorial(num - 1) if num > 1 else num

print(factorial(4))
