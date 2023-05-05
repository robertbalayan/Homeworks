# I put all homework together
dictionary = {
    'Variable': 'Փոփոխական',
    'Declaration': 'Հայտարարում',
    'Assignment': 'Վերագրում',
    'Data types': 'Տվյալների տիպեր',
    'Integer': 'Թվային տիպ',
    'String': 'Տողային տիպ',
    'Boolean': 'Բուլյան տիպ',
    'true': 'Ճշմարիտ',
    'else': 'Հակառակ դեպքում',
    'array': 'Զանգված',
    'if': 'Եթե',
    'false': 'Կեղծ'
}

word = input('Enter an English word to translate to Armenian:\t')

if word in dictionary:
    print(f'The Armenian translation of {word} is: {dictionary[word]}')
else:
    print(f'The given word "{word}" is missing in the dictionary.')
