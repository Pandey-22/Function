# Q14.Write a function to check if a number is prime or not.

def prime():
    n=int(input("entr number"))
    count=0
    i=1
    while i<=n:
        if n%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("prime number")
    else:
        print("composite number")
prime()