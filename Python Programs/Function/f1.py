def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        greatest = n1
    elif n2>n3 and n2>n1:
        greatest = n2    
    else:
        greatest = n3  

    print("The Greatest No is: ",greatest)    


greatest(10,70,30)    