# Q19.What is the output of the following code snippet?
# A. 1 3
# B. 2 3
# C. The program has a runtime error because x and y are not defined.
# D. 3 2
# E. 3 3
# Answer :- E is correct

def func(x = 1, y = 2): 
    x=x+y                                                                                                                                                                                                                                                                                                                
    y=y+1
    print(x,y)
func(y=2,x=1)
