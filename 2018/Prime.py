def prime(n):
   list=[i for i in range(2,n+1)]
   list1=[]
   z=int(n**0.5)
   print (list)
   a=0
   x=2
   for a in range(a,z+1):
      while(x<=n):
         b=list[x]
         c=2
         if((b*c)<=n):
            list.remove(b*c)
            c=c+1
         x=x+1
      list1.append(b)
   print(list)
n=int(input("Enter n"))
prime(n)
