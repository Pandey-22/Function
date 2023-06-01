# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145

def my_fun():
    var=int(input("Enter the number:"))
    a=0
    while var!=a:
        a=a+1
        if var%10==0:
            var=var//10
        else:
            break
    print(var)
my_fun()