def S_L(a):
    SL=0
    L=min(a)
    for i in range(len(a)):
        if a[i]>L:
            SL=L
            L=a[i]
        else:
            SL=max(SL,a[i])
    return SL
print("Second max=",S_L([10,20,4,45,99]))