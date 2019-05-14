import time
def partition(list,low,high):
    list_len=high
    i=low-1
    j=low
    while(j<list_len):
        if(list[j]<list[list_len]):
            i=i+1
            list[i],list[j]=list[j],list[i]
            j=j+1
        if (list[j]>list[list_len]):
            j=j+1
    list[i+1],list[list_len]=list[list_len],list[i+1]
    return i+1
def quicksort(list,low,high):
    if (low<high):
        pivot=partition(list,low,high)
        quicksort(list,low,pivot-1)
        quicksort(list,pivot+1,high)
list=[10,80,30,90,40,50,7,89,0,6,4]
a=len(list)-1
start=time.process_time()
quicksort(list,0,a)
end=time.process_time()
print(list)
print(end-start)
