# def sum(n):
#     sum=0
#     while n>0:    
#         sum=sum+n%10    
#         n=n//10    
#     if sum%2==0:
#         print("sum of digits are even=",sum)
#     else:
#         print("sum of digits are odd=",sum)
# a=int(input("enter number the sum of digits"))
# sum(a)



# a="python"
# b="typhon"
# print(a==b or b!=a)

# a="python"
# b="typhon"
# print(a!=b and b!=a)


# a="code"
# b="type"
# print(a==b or b==a)


# a="code"
# b="type"
# print(a==b and b==a)


# def sum(n):
#     sum=0
#     while n>0:    
#         sum=sum+n%10    
#         n=n//10       
#     if sum%2==0:
#         print("sum of digits are even=",sum)
#     else:
#         print("sum of digits are odd=",sum)
# a=int(input("enter number the sum of digits"))
# sum(a)

# a="insert 0 10"
# x=a.split()
# print(x)

# a="dular"
# x=a.split()
# print(x)


# input=["my","name","is","dular"]
# i=0
# b=[]
# while i<len(input):
#     a=input[i].capitalize()
#     b.append(a)
#     i=i+1
# print(b)


l=[14,8,9,16,2,0,10,56,78,45,23,21,90,60]
l1=[]
while l:
    min=l[0]
    for x in l:
        if x<min:
            min=x
    l1.append(min)
    l.remove(min)
print(l1)