# def calculator(number_x,number_y,operation):
#     l=[]
#     if(operation=="add"):
#         print(number_x+number_y)
#     elif(operation=="sub"):
#         print(number_x-number_y)
#     elif(operation=="divide"):
#         print(number_x/number_y)
#     elif(operation=="multiply"):
#         for i in range(len(number_x)):
#             mul=number_x[i]*number_y[i]
#             l.append(mul)
#         print(l)
#     else:print("invalid request")
# l1=[10,20,30,40]
# l2=[50,60,70,80]
# n=input("enter the operation")
# calculator(l1,l2,n)



def calculator(number_x,number_y,operator):
    l=[]
    if operator=="add":
        print(number_x+number_y)
    elif  operator=="sub":
        print(number_x-number_x)
    elif operator=="divide":
        print(number_x//number_y)
    elif operator=="multi":
        i=0
        while i<len(number_x):
            mul=number_x[i]*number_y[i]
            l.append(mul)
            i=i+1
        print(l)
    else:
        print("invailid request")
l1=[10,20,30,40]
l2=[50,60,70,80]
n=input("enter the number")
calculator(l1,l2,n)