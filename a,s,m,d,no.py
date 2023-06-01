# def calculate(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a//b
#     return add,sub,mul,div
# m=int(input("enter the 1st number"))
# n=int(input("enter the 2nd number"))
# result=calculate(m,n)
# print(result)
# print(type(result))




def calculate(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return add,sub,mul,div
x=int(input("enter the value of x:-"))
y=int(input("enter the value of y:-"))
result=calculate(x,y)
for i in result:
    print(i)