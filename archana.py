# def index_capital(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i].isupper()==True:
#             b.append(i)
#         i=i+1
#     print(b)
# a="ArchAnA"
# index_capital(a)




def list(a,b):
    i=0
    c=[]
    while i<len(a):
        d=a[i][0].upper()+b[i][0].upper()
        c.append(d)
        i=i+1
    print(c)
l=["archana","aariya"]
l1=["singh","pandey"]
list(l,l1)



# def count_capital(a):
#     count=0
#     for i in a:
#         if(i.isupper()):
#             count=count+1
#     print(count)
# b="ArchANa"
# count_capital(b)



# def count_capital(a):
#     count=0
#     count1=0
#     i=0
#     s=a
#     while i<len(a):
#         if(s[i].isupper()):
#             count=count+1
#         elif(s[i].islower()):
#             count1=count1+1    
#         i=i+1
#     print("The capital charactor=",count)
#     print("The small charactor=",count1)
# b="ArchANA"
# count_capital(b)