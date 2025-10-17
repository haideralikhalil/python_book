day = int(input("Enter the day of the week (1-7): "))

if day > 0 and day < 6:
    print("Working Day.")
else:
    if day == 6 or day == 7:
        print("Weekend.")       
    else:
        print("Invalid day entered.")   