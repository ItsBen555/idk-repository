num=int(input('enter a number :'))
a,b=0,1
c=0

for i in range(num):
    a=b  #a=1 a=0 a=1
    b=c #b=0 b=1 b=1
    c=b+a #c=1 c=1 c=2
    print(c)



