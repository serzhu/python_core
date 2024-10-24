from datetime import date, datetime


def get_birthdays_per_week(users):
    # users = [
    #     {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    # ]

    if len(users) == 0:
        print({})

    #d = datetime(2023, 12, 29)
    d = date.today()
    t = datetime.min.time()
    dt = datetime.combine(d,t)
    ts = dt.timestamp()

    # make list of 7 dates: current date and 6 after it, 86_400 seconds in 24 hours
    week = []
    for _ in  range(0,7):
        week.append(datetime.fromtimestamp(ts).date())
        ts += 86_400
    #print(week)

    # check if birthday is in list 'week' and make new list 'birthdays' with this names and (dates -> day of week)
    birthdays = []
    for item in users:
        for key,val in item.items():
            if key == "birthday":
                crnt_year = val.replace(year=d.year)     # change year to the current year in date
                if crnt_year in week:
                    item.update({key:crnt_year.strftime('%A')})
                    birthdays.append(item)
                next_year = val.replace(year=d.year+1)   # change year to the next year in date
                if next_year in week:
                    item.update({key:next_year.strftime('%A')})
                    birthdays.append(item)
    #print(birthdays)
    
    # make finish dictionary with day and birthdays in this day
    result = {}
    for day in week:
        day_of_week = day.strftime('%A')
        for item in birthdays:
            if day_of_week in item['birthday']:
                if day_of_week in result:
                    result[day_of_week].append(item['name'])
                elif day_of_week == 'Saturday' or day_of_week == 'Sunday'and 'Monday' not in result:
                    result['Monday'] = [item['name']]
                elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
                    result['Monday'].append(item['name'])
                else:
                    result.update({day_of_week:[item['name']]})
    #   output {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
