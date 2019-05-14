a=input("Enter Name-")
b=len(a)
s=0
tr=1
for z in range(0,b):
    if(a[z]==" "):
        s=s+1
def asd():
    for t in range(0,b):
        global zt
        zt=t
        if(a[t]==" "):
            sum=a[0:t]
            sum=sum.title()
            print(sum[0]+'.',end=' ')
            break
while(tr==1):
    if(s!=0):
        asd()
        a=a[zt+1:b]
        s=s-1
    else:
        a=a.title()
        print(a)
        tr=0
input()
       
