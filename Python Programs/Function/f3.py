def recursive_sum(n):
    sum = (n*(n+1))/2
    return sum

n = int(input("Enter a Number: "))    
sum = recursive_sum(n)
print("The sum is: ",int(sum))