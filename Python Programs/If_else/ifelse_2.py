from re import M


p = int(input("Enter your Physics Mark: "))
c = int(input("Enter your Chemistry Mark: "))
m = int(input("Enter your Mathematics Mark: "))

t = p+c+m
per = int((t/300)*100)

print("Your Total Mark is ",t," \nwith Percentage of ",per,"%")

if t>=40 and p>=33 and c>=33 and m>=33:
    print("You are Pass.")

else:
    print("You are Fail.")    