# Q10.Create a function that takes 2 positive integers in form, and outputs the sum 
# "4", "5" --> 9
# "34", "5" --> 39

def positive(a,b):
          sum=int(a)+int(b)
          a=str(sum)
          print(repr(a))
i=input("enter the number:")
j=input("enter the number:")
positive(i,j)