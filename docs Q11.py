# Q11.Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)
# Task
# Implement a function named
# generate_range(2, 11, 2) # should return list of [2,4,6,8,10]

# def implement():
#     a=[]
#     for i in range(2,11,2):
#         n=[i]
#         a.append(n[0])
#     print(a)
# implement()


def implement():
    a=[]
    i=2
    while i<=10:
        n=[i]
        a.append(n[0])
        i=i+2
    print(a)
implement()