import datetime
import faker

def current_date():
    print(datetime.date.today())


current_date()

def time_until_jan1():
    print(datetime.datetime.fromisoformat('2022-07-01 00:00:00') - datetime.datetime.now())

time_until_jan1()

def minutes_alive(bday):
    print((datetime.datetime.now() - datetime.datetime.fromisoformat(bday)).total_seconds() / 60)

minutes_alive('1996-04-29 00:00:00')


def today_date():
    now = datetime.datetime.now()
    print(now.date())
    holiday = {'date': datetime.datetime.fromisoformat('2021-08-08 00:00:00'), 'name': 'cat day'}
    print(holiday['date'] - now, 'until', holiday['name'])

today_date()

def age_on_planets(age):
    earth = 31557600
    mercury = 0.2408467 * earth
    venus = 0.61519726 * earth
    return (age / earth, 'earth'), (age/mercury, 'mercury'), (age/venus, 'venus')

fake = faker.Faker()

users = []
def add_user():
    users.append({'name':fake.name(), 'address': fake.address(), 'language_code': fake.language_code()})
add_user()
print(users)
