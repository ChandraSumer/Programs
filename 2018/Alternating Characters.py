a=int(input())
c=0
while(c<a):
    b=str(input())
    d=0
    e=0
    for i in range(d,len(b)-1):
        if(b[d]==b[d+1]):
            b=b[:d]+b[d+2:]
            e=e+1
            d=d-1
    print(b)
    print(e)
    c=c+1
