import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return (math.pi * self.radius) ** 2

    def grow(self):
        return 2 * self.radius

    def get_radius(self):
        return self.radius


# Initialize a placeholder value for input_radius
input_radius = None

while True:
    input_radius = input('Give us a radius: ')

    try:
        # Try to convert the input to a float
        input_radius = float(input_radius)
        break  # Break out of the loop if conversion is successful
    except ValueError:
        print('Please enter a valid float value for the radius.')

my_circle = Circle(input_radius)  # Create a circle with the valid radius

# Example usage:
print("Diameter:", my_circle.calculate_diameter())
print("Circumference:", my_circle.calculate_circumference())
print("Area:", my_circle.calculate_area())

grow = input('Should the circle grow? y/n ')

if grow == 'y':
    new_radius = my_circle.grow()  # Get the new radius from the grow method
    new_circle = Circle(new_radius)  # Create a new Circle with the doubled radius
    print("New radius:", new_circle.get_radius())

    # Example usage:
    print("Diameter:", new_circle.calculate_diameter())
    print("Circumference:", new_circle.calculate_circumference())
    print("Area:", new_circle.calculate_area())
else:
    print('Goodbye!')
