# Q21.What is the output of the following code snippet?
# A. 1 4
# B. 4 1
# C. The program has a runtime error because the local variable ‘num’ referenced before assignment.
# D. 1 1
# E. 4 4
# Answer :- c is correct


num = 1
def func():
    num = num + 3
    print(num)
func()
print(num)
