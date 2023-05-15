class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        self.display()
        print("Section:", self.section)

student = Student("John Doe", 20, "A\n")
student.displayStudent()

#Second
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.Perimeter())
        print("Area:", self.Area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height


# Creating a rectangle object and testing the display method
rectangle = Rectangle(7, 9)
rectangle.display()

# Creating a parallelepiped object and testing the display and Volume methods
parallelepiped = Parallelepipede(3, 4, 6)
parallelepiped.display()
print("Volume:", parallelepiped.Volume())
