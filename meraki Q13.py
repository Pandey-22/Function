def calculator(number_x,number_y,operation):
    if(operation=="add"):
        print(number_x+number_y)
    elif(operation=="sub"):
        print(number_x-number_y)
    elif(operation=="divide"):
        print(number_x/number_y)
    elif(operation=="multiply"):
        print(number_x*number_y)
    else:
        print("invalid request")
n=int(input("enter the 1st number"))
m=int(input("enter the 2nd number"))
o=input("enter the operation")
calculator(n,m,o)