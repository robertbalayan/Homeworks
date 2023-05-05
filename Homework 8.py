import random
# first task

for i in range(5):
    print(" ")
    for j in range(i + 1):
        print(j + 1, end=" ")

print("\n_____________________________________________________________________________________")

# Second task
number = [12, 75, 150, 180, 145, 575]

for x in range(len(number)):
    if number[x] == 500:
        print("Stopping program")
        break

    elif number[x] > 150:
        continue

    elif number[x] % 5 == 0:
        print(number[x])


print("\n_____________________________________________________________________________________")
# third task
x = input("Input your word:\t")
print(len(x))
print("\n_____________________________________________________________________________________")
#Fourth Task
print("\n_____________________________________________________________________________________")
#Fifth task
for i in range(5):
    print("")
    for j in range(i+1):
        print("*", end=" ")
for a in range(5, 0, -1):
    print("")
    for b in range(a-1):
        print("*", end=" ")
print("\n_____________________________________________________________________________________")
# Sixth task


Dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

for value in Dictionary.values():

    if isinstance(value, str):
        length = len(value)

        print(f"Length of '{value}': {length}")
print("\n_____________________________________________________________________________________")
# Seventh Task

sen = input("Input your sentence:\t").lower().split()
wscount = {}
for word in sen:
    if word in wscount:
        wscount[word] += 1
    else:
        wscount[word] = 1
print(wscount)
for key, value in wscount.items():
    print(f"word:{ key},count:{ value}")
print("\n_____________________________________________________________________________________")
#Nineth task
my_list = [random.randint(-10, 10) for _ in range(10)]


positive_count = 0
negative_count = 0

for num in my_list:

    if num > 0:
        positive_count += 1

    elif num < 0:
        negative_count += 1


print("List of random numbers:", my_list)
print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)