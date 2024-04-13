mark = int(input("Enter Your Secured Mark: "))

per = int((mark/600)*100)

if per>=90 and per<=100:
    grade = "EX"
elif per>=80 and per<=90:
    grade = "A"
elif per>=70 and per<=80:
    grade = "B"   
elif per>=60 and per<=70:
    grade = "C"
elif per>=50 and per<=60:
    grade = "D"         
else:
    grade = "F"   

print("Your Grade is: ",grade)    

