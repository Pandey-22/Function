# Q20.What is the output of the following code snippet?
# A. 1 3
# B. 3 1
# C. The program has a runtime error because x is not defined.
# D. 1 1
# E. 3 3
# Answer :-B is correct

num=1
def func():
    num=3
    print(num,end=" ")
func()
print(num)

