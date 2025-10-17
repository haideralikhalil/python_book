class Student:
    name = "Unknown"
    age = 0

st1 = Student()
st2 = Student()

st1.name = "Alice"
st1.age = 20    

st2.name = "Bob"
st2.age = 22

print(f"Student#1: {st1.name} ({st1.age} years old)")
print(f"Student#2: {st2.name} ({st2.age} years old)")
