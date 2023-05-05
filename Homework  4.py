# First Task
a = input("Your Word:\t")

length = len(a) // 2
print(a[length - 1],
      a[length],
      a[length + 1])
print("\n__________________________________________________________________________________________")
# Second Task
string = input("Input your word:\t")
if len(string) < 3:
    print(string)
elif string[-3:] == 'ing':
    print(string + 'ly')
else:
    print(string + 'ing')
print("\n__________________________________________________________________________________________")
# Third Task
str = input("Input youre word to see if its plaindrome or no:\t")

reverse = reversed(str)

if list(str) == list(reverse):
    print("Your word is Palindrom")
else:
    print("Youre word is not palindrom !")
print("\n__________________________________________________________________________________________")
# Fifth Task
x = input("Input your word:\t")
print("This is your word in UPPER case")
print(x.upper())
print("This is your word in lower case")
print(x.lower())
print("\n__________________________________________________________________________________________")
