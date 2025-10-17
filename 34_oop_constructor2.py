class Student:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
st1 = Student("Alice", 20 )
st2 = Student("Bob", 22 )

st1.display()
st2.display()