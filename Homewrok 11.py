#First Task
def divide_numbers():
    a = int(input("Input:\t"))
    b = int(input("Input:\t"))
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    return result
print(divide_numbers())
print("\n_________________________________________________________________________________________________________________________________________")
#Second Task
def sum_numbers():
    numbers = input("Input:\t")
    try:
        total = sum(numbers)
        return total
    except TypeError:
        return None
print(sum_numbers())

# Third Task
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:

        return None

print(read_file('example.txt'))
print("\n_________________________________________________________________________________________________________________________________________")
# fourth Task
def product_of_ends(nums):
    try:
        first = nums[0]
        last = nums[-1]
        return first * last
    except IndexError:
        return None

user_input = input("Input a list of integers separated by commas: ")
nums = [int(num) for num in user_input.split(',')]

print(product_of_ends(nums))