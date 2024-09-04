# Q29. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

# for loop 
def sum_of_multiples(limit):
    sum=[]
    for number in range(1, limit):
        if number%3==0:
            sum.append(number)
        elif number%5==0:
            sum.append(number)
    print(sum)
n=int(input("enter the limit:"))
sum_of_multiples(n)


# while loop 
def sum_of_multiples(limit):
    sum=[]
    i=1
    while i<=limit:
        if i%3==0:
            sum.append(i)
        elif i%5==0:
            sum.append(i)
        i=i+1
    print(sum)
n=int(input("enter the limit:"))
sum_of_multiples(n)