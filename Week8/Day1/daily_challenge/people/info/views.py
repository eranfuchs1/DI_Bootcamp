from django.shortcuts import render

# Create your views here.


def people(request, X=None):
    people = [
            {
                'id': 1,
                'name': 'Bob Smith',
                'age': 35,
                'country': 'USA'
                },
            {
                'id': 2,
                'name': 'Martha Smith',
                'age': 60,
                'country': 'USA'
                },
            {
                'id': 3,
                'name': 'Fabio Alberto',
                'age': 18,
                'country': 'Italy'
                },
            {
                'id': 4,
                'name': 'Dietrich Stein',
                'age': 85,
                'country': 'Germany'
                }
            ]
    context = {}
    if X == None:
        context['people'] = sorted(people, key = lambda i: i['age'])
        return render(request, 'all_people.html', context)
    else:
        context['people'] = people[X - 1]
        return render(request, 'people.html', context)
