# Q34. Write a function which converts the input string to uppercase.
# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def list(a):
    i=0
    max=0
    max2=0
    while i<len(a):
        if a[i]>=max:
            max=a[i]
        elif a[i]>=max2 and a[i]!=max:
            max2=a[i]
        i=i+1
    # print(max)
    # print(max2)
    return max+max2
print(list([10,14,2,23,19]))
print(list([99,2,2,23,19]))