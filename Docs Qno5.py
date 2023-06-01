# Q5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

# for loop 
# def unique_list(l):
#     x=[]
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x
# print(unique_list([1,2,3,3,3,3,4,5])) 


# while loop 
def unique_list(l):
    x=[]
    a=1
    while a<len(l)-2:
        if a not in x:
            x.append(a)
        a=a+1
    return x
print(unique_list([1,2,3,3,3,3,4,5]))