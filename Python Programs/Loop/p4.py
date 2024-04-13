
n = int(input("Enter a No: "))
flag = False

if n == 1:
    print("This no is not a prime number")

else:
    for i in range(2, n):
        if (n%i)==0:
            flag = True

if flag == True:
    print("This number is not a prime number")
else:
    print("This number is a prime number")                

    