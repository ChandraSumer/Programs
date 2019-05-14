import random
import time
def random1():
	n=int(input("Enter n: "))
	list=[random.randint(0,10000) for i in range(0,n)]
	bubblesort(list)
def bubblesort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    search=int(input("Enter Element to be searched: "))
    b_s(list,search)

def b_s(list,search):
    x=0
    start=0
    end=len(list)-1
    start_time = time.time()
    while start<end:
        mid=int((start+end)/2)
        if search==list[mid]:
            x=1
            break
        elif search<list[mid]:
            end=mid-1
        elif search>list[mid]:
            start=mid+1
    end_time = time.time()
    if x==0:
        print("Element not present in the list. ")
    else:
        print("The element is at postion. ", mid)
    print('Duration:',(end_time - start_time)*1000,' microseconds')
random1()
