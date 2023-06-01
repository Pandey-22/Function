def perfect(n):
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        print("Perfect number")
    else:
        print("Not Perfect number")
a=int(input("enter the number"))
perfect(a)