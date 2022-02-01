mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

sum=mark1+mark2+mark3+mark4+mark5

avg=sum/5

percentage=(sum*100)/500

print("Avg marks:",avg)

print(" percentage of marks:", percentage)

if(avg>=80 and avg<=100):
    print("A+")
elif(avg>=70 and avg<=80):
    print("A")
elif(avg>=60 and avg<=70):
    print("B+")
elif(avg>=50 and avg<=60):
    print("B")
elif(avg>=40 and avg<=50):
    print("C")
else:
    print("F")
