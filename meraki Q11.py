# def check_number(a,b):
#     if a%2==0 and b%2==0:
#         print("both number is even")
#         print(a//2,b//2)
#     else:
#         print("both number is not even")
# x=int(input("enter the 1st number"))
# y=int(input("enter the 2nd number"))
# check_number(x,y)




# def check_number_list(a,b):
#     for i in range(len(a)):
#         if a[i]%2==0 and b[i]%2==0:
#             print("both number is even")
#         else:
#             print("both number is not even")
# l1=[10,13,20,21,22]
# l2=[16,18,22,21,24]
# check_number_list(l1,l2)



def check_number(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both is number even")
        else:
            print("both number is not even")
        i=i+1
l1=[10,13,20,21,22]
l2=[16,18,22,21,24]
check_number(l1,l2)