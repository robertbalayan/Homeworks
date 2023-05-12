# First Task
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(5, 3)

# calculate the area of the rectangle
area = rectangle.calculate_area()
print("Area of rectangle:", area)

# calculate the perimeter of the rectangle
perimeter = rectangle.calculate_perimeter()
print("Perimeter of rectangle:", perimeter,"\n")
#second Task
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def print_balance(self):
        print("Account balance:", self.balance)

account = BankAccount("1234", 1000.0)


account.deposit(500.0)


account.withdraw(200.0)


account.print_balance()
