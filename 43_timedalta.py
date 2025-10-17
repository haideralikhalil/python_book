from datetime import datetime, timedelta

today = datetime.now()
print("Today's date is:", today)
print(today + timedelta(days = 15))
print(today + timedelta(weeks = 5))
