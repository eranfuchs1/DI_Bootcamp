from .models import Bookings
from datetime import date
from datetime import timedelta


def get_bookings(room_number):
    return Bookings.objects.filter(room=room_number, approved=True)


def day_is_vacancy(room_number, day, bookings):
    for booking in bookings:
        if day >= bookings.check_in_date and day <= bookings.check_out_date:
            return False
    return True


def get_vacancies(room_number, bookings=None, days_ahead=30, day_start=date.today()):
    bookings = bookings if bookings else get_bookings(room_number)
    days = [day_start + timedelta(days=i) for i in range(days_ahead)]
    return list(filter(lambda day: day_is_vacancy(room_number, day, bookings), days))


def is_vacancy(room_number, check_in_date, check_out_date, bookings=None):
    bookings = bookings if bookings else get_bookings(room_number)
    check_in_delta = check_in_date - check_out_date
    return len(get_vacancies(room_number, bookings, check_in_delta.days, check_in_date)) == check_in_delta.days

def is_valid_check_in_out_dates(check_in_date, check_out_date):
    check_in_delta = check_in_date - check_out_date
    if check_in_delta.days == 0:
        return False
    return True