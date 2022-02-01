import math
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = (b*b) - (4*a*c)

if(d==0):
    x=-b/(2*a)
    print("Roots are real & equal:",x)
    
elif(d>0):
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print("Roots are real & unequal:",x1,x2)
    
else:
    print("Roots are imaginary")
