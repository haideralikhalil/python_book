marks = int(input("Enter your marks: "))
if marks >= 50:
    print("You have passed.")
    if marks >= 90:
        print("You have achieved a distinction.")
    else:
        print("You have not achieved a distinction.")   
else:
    print("You have failed.")
    if marks < 0:
        print("Invalid marks entered.")
    else:
        print("You need to score at least 50 to pass.")