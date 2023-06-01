# Q22.What is the output of the following code snippet?
# A. 1 4
# B. 4 1
# C. The program has a runtime error because the local variable ‘num’ referenced before assignment.
# D. 1 1
# E. 4 4 
# Answer :- E is correct

num = 1
def func():
    global num
    num = num + 3
    print(num,end=" ")
func()
print(num)
