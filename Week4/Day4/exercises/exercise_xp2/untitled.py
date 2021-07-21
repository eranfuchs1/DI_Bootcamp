def get_age(day, month, year, curr_year=2021, curr_month=7, curr_day=21):
    return curr_year - year - (1 if ((curr_month == month and day >= curr_day) or curr_month < month) else 0)

def can_retire(gender, date_of_birth):
    return ((67 if gender=='male' else 62) - get_age(*map(int, date_of_birth.split('/')))) < 0

print(can_retire('male', '4/3/1960'))


def addition_digits(x):
    return sum([int(f'{x}' * i) for i in range(1,5)])

print(addition_digits(3))
