def Triangle():
    import math
    a = float(input('Enter first value '))
    b = float(input('Enter second value: '))
    c = float(input('Enter third value '))
    
    if((a+b)>c and (b+c)>a and (c+a)>b):
        s = (a + b + c) / 2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("The area of the triangle is",area)
    else:
        print("Triangle is not possible")
        
Triangle()
