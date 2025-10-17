x = 100
def func():
    global x
    x = 50
    print("Inside func():", x)  


func()
print("Outside:", x)
