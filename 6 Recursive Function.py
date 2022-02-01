def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

    
terms = int(input())
if terms <= 0:
    print("Enter a positive integer")
else:
    for i in range(terms):
        print(fibo(i))
