n = 4

#decline triangle
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()

#inverted decline triangle
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()
