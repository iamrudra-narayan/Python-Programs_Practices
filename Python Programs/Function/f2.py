def temp_converter(c):
    f  = (c * (9/5))+32
    return f

c = int(input("Enter celcius Temperature: "))
f = temp_converter(c)    
print("temperature in Farenhite is: ",f)