#I put all homework togheter here
A = []
B = []

for i in range(10):
    num = int(input("Enter a number:\t"))
    A.append(num)

for i in range(10):
    num = int(input("Input  a number for b list :\t"))
    B.append(num)
A_set = set(A)
B_set = set(B)


print("A: ", A_set)
print("B: ", B_set)
print("A == B: ", A_set == B_set)
print("A union B: ", A_set.union(B_set))
print("A intersection B: ", A_set.intersection(B_set))
print("A difference B: ", A_set.difference(B_set))
print("B difference A: ", B_set.difference(A_set))