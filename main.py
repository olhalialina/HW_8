from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    dict_date = {today.strftime('%A'): today}
    for el in range(1, 7):
        today += timedelta(days=1)
        dict_date[today.strftime('%A')] = today

    result = {}

    for el_users in users:
        dt_users = el_users["birthday"]

        for weekday in dict_date:
            dt_today = dict_date[weekday]

            if not (dt_today.month == dt_users.month
                    and dt_today.day == dt_users.day):
                continue

            if weekday in ('Sunday', 'Saturday'):
                if 'Monday' in result:
                    result['Monday'].append(el_users["name"])
                else:
                    result['Monday'] = [el_users["name"]]

            else:
                if weekday in result:
                    result[weekday].append(el_users["name"])
                else:
                    result[weekday] = [el_users["name"]]

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan", "birthday": datetime(1976, 11, 24).date()},
        {"name": " Koum", "birthday": datetime(1976, 11, 22).date()},
        {"name": "JK", "birthday": datetime(1976, 11, 25).date()},
        {"name": "Heho", "birthday": datetime(1976, 11, 26).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
