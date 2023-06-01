def add_list(a,b):
    i=0
    d=[]
    while i<len(a):
        c=a[i]+b[i]
        d.append(c)
        i=i+1
    print(d)
c=["m","na","i","Aari"]
e=["y","me","s","ya"]
add_list(c,e)