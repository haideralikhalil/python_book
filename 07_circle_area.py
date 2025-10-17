# Get input from user and convert it to a float (decimal number)
radius = float(input("Enter the radius of the circle: "))

# Calculate the area (π * r^2)
area = 3.14159 * (radius ** 2)

# Calculate the circumference (2 * π * r)
circumference = 2 * 3.14159 * radius

# Display the results
print(f"Area = {area:.2f}")           # :.2f means format to 2 decimal places
print(f"Circumference = {circumference:.2f}")