#First Task
count = int(input("Input count of numbers:\t"))
l = []
for x in range(count):
    num = int(input(f"input {x + 1} number:\t"))
    l.append(num)
print("Your numbers is\n", l)

for y in range(len(l)):
    l[y] = l[y] ** 2
print("The Square of your numbers is\n", l)
print("\n__________________________________________________________________________________________")
#Second Task
x = 0
a = int(input("Input your number:\t"))
b = int(input("Input your second number:\t"))
c = int(input("Input your third number:\t"))
d = int(input("Input your fourth number:\t"))
list = [a,b,c,d]
for i in list:
    x += i
print(x)
print("\n__________________________________________________________________________________________")
#Third Task
w = int(input("Input your number:\t"))
x = int(input("Input your second number:\t"))
y = int(input("Input your third number:\t"))
z = int(input("Input your fourth number:\t"))
num = [w,x,y,z]

# Calculate the product of all elements in the list
product = 1
for num in num:
    product *= num

# Print the result
print("The product of all elements in the list is:", product)
print("\n__________________________________________________________________________________________")
#Fourth Task
a = int(input("Input your number:\t"))
b = int(input("Input your second number:\t"))
c = int(input("Input your third number:\t"))
d = int(input("Input your fourth number:\t"))
list = [a, b, c, d]

if 20 in list:
    index = list.index(20)
    list[index] = 200
    print("Replaced 20 with 200 at index", index)
else:
    print("20 not found in the list")