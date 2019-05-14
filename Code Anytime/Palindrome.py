def lvl1():
    a=input("Enter a String")
    b=len(a)-1
    print (b)
    c=0
    d=0
    while (b>c):
        if (a[b]==a[c]):
            b=b-1
            c=c+1
        else:
            d=d+1
            break
    if (d==1):
        print ("Palindrome. Not!!!")
    elif(d==0):
        print("palindrome")
def lvl11():
    a=int(input("enter string-"))
    print (a)
    print (type(a))
