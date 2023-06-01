# def calcu(a,b,c):
#     i=1
#     while i<=a:
#         if c=="+":
#             print(a+b)
#         elif c=="-":
#             print(a-b)
#         elif c=="*":
#             print(a*b) 
#         elif c=="%":
#             print(a%b)
#         else:
#             print("I can't do anything with the number")
#         break
# n=int(input("enter the 1st number"))
# m=int(input("enter the 2nd number"))
# o=input("enter the operator")
# calcu(n,m,o)



def add(a,b):
    a=a+b
    print(a)
    return a
def sub(c,n):
    c=c-n
    print(c)
    return
def mul(s,d):
    s=s*d
    print(s)
    return
def div(j,l):
    j=j//l
    print(j)
    return
def c():
    n=int(input("enter the 1st number"))
    m=int(input("enter the 2nd number"))
    o=input("enter the operator")
    if o=="+":
        add(n,m)
    elif o=="-":
        sub(n,m)
    elif o=="*":
        mul(n,m)
    elif o=="//":
        div(n,m)
c()