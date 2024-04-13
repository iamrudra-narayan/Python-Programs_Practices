a = int(input("Enter 1st No: "))
b = int(input("Enter 2nd No: "))
c = int(input("Enter 3rd No: "))
d = int(input("Enter 4th No: "))

if a>b and a>c and a>d:
    print("a is greatest.")

elif b>a and b>c and b>d:
    print("b is greatest.")

elif c>a and c>b and c>d:
    print("c is greatest.")

else:
    print("D is greatest.")        
