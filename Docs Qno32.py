# Q32.Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 
# 2 with the exponent ranging from 0 to n (inclusive). 
# if n=0 output=[1]
# if n=1 output=[1,2]
# if n=2 output=[1,2,4]

# for loop 
# def powers_of_two(n):
#     o=[]
#     for i in range(n+1):
#         o.append(2**i)
#     print(o)
# a=int(input("enter the number"))
# powers_of_two(a)



# while loop 
def powers_of_two(n):
    a=[]
    i=0
    while i<n+1:
        a.append(2**i)
        i=i+1
    print(a)
b=int(input("enter the number"))
powers_of_two(b)