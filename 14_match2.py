day = int(input("Enter the day of the week (1-7): "))
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Weekday")
  case 6 | 7:
    print("Weekend")
  case _:
    print("Invalid day entered.")