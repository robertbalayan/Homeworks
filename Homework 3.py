# First Task
sum = 0
count = 0
for i in range(11, 100):
    if i % 4 == 1:
        sum += i
        print(i)

print("Total Numer is ", sum)
print("\n__________________________________________________________________________________________")
# Second Task
x = float(input("Enter the outside temperature:\t"))

if x <= 5:
    print("Its Really cold, so make sure you wear a coat")
elif x <= 20:
    print("Its Warm, Buy you should wear Jacket")
elif x <= 50:
    print("Ohh realy hot outside ")
print("\n__________________________________________________________________________________________")
# Third Task A
x = 0
while x in range(40):
    x += 1
    if x % 4 == 0:
        print("Number", x)
print("\n__________________________________________________________________________________________")
# Third Task B
i = 7
sum = 0
for i in range(30):
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)
print("\n__________________________________________________________________________________________")
# Fourth Task
for i in range(100, 601):
    if i % 3 == 0 and i % 11 == 0 or i % 7 == 1:
        print(i)
print("\n__________________________________________________________________________________________")
# Fifth Task
a = int(input("Input your start number:\t"))
b = int(input("Input your stop number:\t"))

for i in range(a, b):
    if i % 7 == 0:
        print(i)
