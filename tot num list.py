def total_list_num(a):
    i=0
    sum=0
    num=0
    while i<len(a):
        if type (a[i]) is list:
            j=0
            while j<len(a[i]):
                n=a[i][j]
                sum=sum+n
                j=j+1
        else:
            num=num+a[i]
        i=i+1
    total=sum+num
    print("Total number of list=",total)
a=[2,3,[5,8,8],2,8]
total_list_num(a)