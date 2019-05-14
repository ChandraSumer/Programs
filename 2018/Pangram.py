list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
a=input()
a=a.lower()
b=len(a)
c=0
while(c<b):
    if(a[c] in list):
        d=a[c]
        list.remove(d)
    c=c+1
if(len(list)==0):
    print('pangram')
else:
    print('not pangram')
