#First Task
file = open("Poem.txt", 'r')
for line in file:
    print(line.strip())
print("\n______________________________________________________________________________________")
#Third Task
text = input("Input Something:\t")
file = open("TextAdder.txt", 'a')
file.write(text)
file.close()

file = open("TextAdder.txt", 'r')
print(file.read())
file.close()
#Fourth Task
file_2 = open("story.txt", 'w')
for line_2 in file_2:
    words = line_2.split()
    for word in words:
        if len(word) < 4:
            print(word)
file_2.close()