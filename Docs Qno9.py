# Q9.Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def printValues():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    a=l[:5]
    b=l[-5:]
    print((a,b))
printValues()