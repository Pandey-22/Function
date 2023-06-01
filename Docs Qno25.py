# Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
# Example:
# list1 = [2,-7,5,-64,-14]
# Output: pos = 2, neg = 3

def numbers(list):
    p=0
    n=0
    for i in list:
        if i>0:
            p=p+1
        else:
            n=n+1
    print("Positive number=",p,"Negative number=",n)
numbers([2,-7,5,-64,-14])
        