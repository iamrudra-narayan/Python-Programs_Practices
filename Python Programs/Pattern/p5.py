n = 4

#incline triangle
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

#inverted incline triangle
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=' ')
    print()
