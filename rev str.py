# def rev_str():
#     a="My Name is Aariya"
#     b=a.split()
#     i=-1
#     d=""
#     while i>=-len(b):
#         c=b[i]
#         j=-1
#         while j>=-len(c):
#             f=c[j]
#             d=d+c[j]
#             j=j-1
#         d=d+" "
#         i=i-1
#     print(d)
# rev_str()




def fname(a):
    i=0
    c=[]
    f=[]
    while i<len(a):
        b=a.count(a[i])
        if a[i] not in f:
            f.append(a[i])  
            d=a[i]+":"+str(b)
            c.append(d)
        i=i+1
    print(c)
b="dularpanndey"
fname(b)