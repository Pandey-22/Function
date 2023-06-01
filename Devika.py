# def sum_all_items():
#     a=[2,3,[5,8,8],2,8]
#     i=0
#     sum=0
#     num=0
#     while i<len(a):
#         if type (a[i]) is list:
#             j=0
#             while j<len(a[i]):
#                 n=a[i][j]
#                 sum+=n
#                 j=j+1
#         else:
#             num+=a[i]
#         i=i+1
#     total=sum+num
#     print(total)
# sum_all_items()






# a=[3,4,8,5,4,3,8,11,11,12,8]
# b=[]
# for i in a:
#     n=a.count(i)
#     if n>1:
#         if b.count(i)==0:
#             b.append(i)
# print(b)


# def count_dupli():
#     a=[3,4,8,5,4,3,8,11,11,12,8]
#     b=[]
#     i=0
#     while i<=len(a):
#         n=a.count(i)
#         if n>1:
#             if b.count(i)==0:
#                 b.append(i)
#         i=i+1
#     print(b)
# count_dupli()





# a=[3,4,8,5,4,3,8,11,11,12,8]
# i=3
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i=i+6
# print(b)


# def name(a):
#     i=0
#     while i<len(a)-3:
#         i=i+1
#     print(i)
# b="My name"
# name(b)




# def even_odd(list1):
#     i=0
#     a=[]
#     b=[]
#     while i<len(list1):
#         if list1[i]%2==0:
#             a.append(list1[i])
#         elif list1[i]%2!=0:
#             b.append(list1[i])
#         i=i+1
#     p=sum(a)
#     s=sum(b)
#     print([s,p]) 
# list=[5,2,3,8,9,10]
# even_odd(list)






def ma_x(a):
    i=0
    while i<len(list1):
        i=i+1
    b=max(a)
    print(b)
list1=[5,2,3,8,9,10]
ma_x(list1)