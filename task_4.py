from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict]):
    """
    Повертає список користувачів, у яких день народження
    настає протягом наступних 7 днів включно з поточним днем.
    Якщо день народження припадає на вихідний —
    дата привітання переноситься на найближчий понеділок.
    """
    today = datetime.today().date()
    result = []

    for user in users:

         # Перетворюємо дату народження з рядка у date
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        # If birthday already pass this year - add one year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # If days to birthday are within given range (7 days) append entry to result list
        days_to_birthday = (birthday_this_year - today).days
        if days_to_birthday <= 7:
            congratulation_day = birthday_this_year

            # If birthday on weekends (5 or 6) - change congratulation day
            if congratulation_day.weekday() == 5:
                congratulation_day += timedelta(days=2)
            elif congratulation_day.weekday() == 6:
                congratulation_day += timedelta(days=1)


            # Appending the entry to result
            result.append({
                'name': user["name"],
                'congratulation_date': congratulation_day.strftime("%Y.%m.%d")
            })
    return result