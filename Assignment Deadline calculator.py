week= input("How long do you have left")
week_as_int = int(week)

week_remaining = 52 - week_as_int
days_remaining = week_remaining * 365
hours_remaining = week_remaining * 8760
minutes_remaining = week_remaining * 525600

Information = f"You have {days_remaining} days, {hours_remaining} hours, and {minutes_remaining} minutes before your assignment deadline"

print(Information)
