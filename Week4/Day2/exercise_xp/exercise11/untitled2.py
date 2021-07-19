person_details = [person_detail for person_detail in input('enter your names followed by whitespcae and age, seperated by commas: ').split(',')]

allowed = [person_detail.split(' ')[0] * flag for flag, person_detail in zip([age <= 21 and age >= 16 for age in [int(person_detail.split(' ')[1]) for person_detail in person_details]], person_details)]

for key, value in enumerate(allowed):
    if not value:
        del allowed[key]

print(allowed)
