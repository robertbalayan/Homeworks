#First task
x = int(input("input number:\t"))

if x % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd ")

if x % 2 == 0 and x % 3 == 0:
    print("Your number also divides by 2 and 3 ")
elif x % 3 == 0:
    print("and your number also divides by 3")
elif x % 2 == 0:
    print("and your number also divides by 2")
print("\n__________________________________________________________________________________________")
#Second Task
x = int(input("input first number:\t"))
y = int(input("input second number:\t"))

if x == y:
    print(x,y,sep="-")
    print("Both are equal")
elif x > y:
    print(x,y,sep="-")
    print("First number is the Biggest")
elif x < y:
    print(x,y,sep="-")
    print("Second number is the biggest")
print("\n__________________________________________________________________________________________")
#Third Task
a = 15
b = 97

if a == b:
    print("Both are equal")
elif a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
print("\n__________________________________________________________________________________________")
#Fourth Task
x = int(input("input number:\t"))

if x % 5 == 0 and x % 7 == 0:
    print("Your number  divides by 7 and 5 ")
elif x % 5 == 0:
    print(" Your number divides by 5")
elif x % 7 == 0:
    print("Your number divides by 7")
else:
    print("Your Number doesnt divides by 5 or 7")