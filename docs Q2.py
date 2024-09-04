# Q2.Write a Python function to find the Max of three numbers.

def fun(a,b,c):
    if a>b and a>c:
        print("max number:-",a)
    elif b>a and b>c:
        print("max number:-",b)
    elif c>a and c>b:
        print("max number:-",c)
    else:
        print("all numbers are different") 
A=int(input("enter the 1st number:-"))
B=int(input("enter the 2nd number:-"))
C=int(input("enter the 3rd number:-"))
fun(A,B,C)