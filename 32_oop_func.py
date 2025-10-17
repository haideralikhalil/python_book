class Student:
    name = None
    age = None

    def set(self, st_name, st_age):
        self.name = st_name
        self.age = st_age

    def display(self):
        print(f"{self.name} is {self.age} years old.")
    
st1 = Student()
st2 = Student()

st1.set("Charlie", 23)
st2.set("Diana", 21)

st1.display()
st2.display()