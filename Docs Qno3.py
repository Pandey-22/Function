# Q3.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20.

# while loop 
def sum(numbers):
    total=0
    x=1
    while x<len(numbers)+1:
        x=x+1
        total=total+x
    return total
print(sum((8,2,3,0,7)))


# for loop 
# def sum(numbers):
#     total=0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8,2,3,0,7)))