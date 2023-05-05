# first or Second task idk and I cannot do Bubble Sort
string_list = ['hello', 'world', 'python', 'list', 'comprehension']
length_list = [len(s) for s in string_list]
print(length_list)
print("\n________________________________________________________________________________________________________")
# Second task
integer_list = [4, 9, 16, 25, 36]
sqrt_list = [num**0.5 for num in integer_list]
print(sqrt_list)
print("\n________________________________________________________________________________________________________")
# third task
square = lambda num_list: [num**2 for num in num_list]
integer_list = [1, 2, 3, 4, 5]
square_list = square(integer_list)
print(square_list)