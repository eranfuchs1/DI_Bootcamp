month = int(input('enter a month (1-12)'))
if month <= 2 or month == 12:
    print('Winter')
elif month >= 9:
    print('Autumn')
elif month >= 6:
    print('Summer')
else:
    print('spring')
