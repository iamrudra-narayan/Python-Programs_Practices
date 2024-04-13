a = 12
b = 18
c = 14
d = 15

if a>b and a>b and a>d:
    greater = a
elif b>a and b>c and b>d:
    greater = b
elif c>a and c>b and c>d:
    greater = c
else:
    greater = d

print(greater)