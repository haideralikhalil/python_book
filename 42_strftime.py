from datetime import datetime

current_date = datetime.now()
print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
print(current_date.strftime("%d/%m/%Y"))

print(current_date.strftime("%B %dth, %Y"))
print(current_date.strftime("%A, %B %d, %Y"))

