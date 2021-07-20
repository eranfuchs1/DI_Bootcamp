import sys

exercise_chosen = 0
if len(sys.argv) > 1:
    exercise_chosen = int(sys.argv[1])
else:
    print(f'usage: python {sys.argv[0]} <exercise number>')

# exercise 1
if exercise_chosen == 1:

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    print({key: value for key, value in zip(keys,values)})


# exercise 2
elif exercise_chosen == 2:
    family = {key: int(value) for key, value in[item.split(':') for item in [string for string in input('names:ages,').split(',')]]}

    cost = sum(10 if age <= 12 else 15 for age in family.values() if age > 2)
    print(f'the total price is {cost}$')


# exercise 3

elif exercise_chosen == 3:
    brand = {
    'name': "Zara",
    'creation_date': 1975,
    'creator_name': ["Amancio", "Ortega", "Gaona"], 
    'type_of_clothes': ["men", "women", "children", "home"], 
    'international_competitors': ["Gap", "H&M", "Benetton"], 
    'number_stores': 7000, 
    'major_color':
    {"France":[  "blue",  ],
    "Spain": [ "red", ] ,
    "US": [ "pink", "green" ],}}
    brand['number_stores'] = 2
    print('zara\'s clients are', end=' ')
    for client in brand['type_of_clothes'][:-2]:
        print(client, end=', ')
    print(f'and {brand["type_of_clothes"][-2]}')
    brand.update({'country_creation': 'Spain'})
    if 'international_competitors' in brand:
        brand['international_competitors'].append('Desigual')
    del brand['creation_date']
    print(brand['international_competitors'][-1])
    print(brand['major_color']['US'])
    print(len(brand))
    print(brand.keys())
    more_on_zara = {
            'creation_date': 1975,
            'number_stores': 10_000
            }
    print(more_on_zara)
    brand.update(more_on_zara)
    print(brand['number_stores'])
    print('''
number of stores changes because update method updates the values for the values of the keys in the given
dictionary (adding the key value pairs for the keys that don\'t exist).''')
elif exercise_chosen == 4:
    users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
    disney_users_A = {key: value for value, key in enumerate(users)}
    print(disney_users_A)
    disney_users_B = {key: value for key, value in enumerate(users)}
    print(disney_users_B)
    users.sort()
    disney_users_C = {key: value for value, key in enumerate(users)}
    print(disney_users_C)
    disney_users_A = {key: value for value, key in enumerate(users) if 'i' in key or key[0].lower() in 'mp'}
    print(disney_users_A)
