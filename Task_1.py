from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).strftime("%A")

            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"

            birthdays[weekday].append(name)

    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")

users = [
  {"name": "Bill Gates", "birthday": datetime(1955, 2, 24)},
  {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 1)},
  {"name": "Jan Koum", "birthday": datetime(1976, 3, 1)},
  {"name": "Jill Valentine", "birthday": datetime(1979, 2, 26)},
]

get_birthdays_per_week(users)