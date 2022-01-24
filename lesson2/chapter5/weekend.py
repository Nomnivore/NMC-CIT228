import datetime


weekdays = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")

now = datetime.date.today()

day_of_week = now.weekday()

today = weekdays[day_of_week]

days_until_weekend = 6 - day_of_week

print("There are ", days_until_weekend - 1, " days until the weekend.")
quote_printed = False

for left in weekdays[day_of_week:days_until_weekend]:
    if today == "Sunday" and not quote_printed:
        print(left, " Sunday is a day of rest")
        quote_printed = True
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and not quote_printed:
        print(left, "Hard at work.")
        quote_printed = True
    elif today == "Thursday" and not quote_printed:
        print(left, "It's Thursday. Finishing up the last bits of work.")
        quote_printed = True
    elif not quote_printed:
        print(left, "Yay, its time for the weekend!")
        quote_printed = True
    else:
        print(left)
