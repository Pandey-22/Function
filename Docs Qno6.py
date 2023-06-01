# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1,2,3,4,5,6,7,8,9]
# Expected Result : [2,4,6,8].

# for loop 
# def even_num(l):
#     enum=[]
#     for n in l:
#         if n%2==0:
#             enum.append(n)
#     return enum
# print(even_num([1,2,3,4,5,6,7,8,9]))

# while loop 
def even_num(l):
    enum=[]
    n=0
    while n<len(l):
        n=n+1
        if n%2==0:
            enum.append(n)
    return enum
print(even_num([1,2,3,4,5,6,7,8,9]))