import time
def b_s(list,search):
    x=0
    start=0
    end=len(list)-1
    start_time = time.time()
    print(start_time)
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
    print(end_time)
    print('Duration:',(end_time - start_time))
    if x==0:
        print("Element not present in the list")
    else:
        print("The element is at postion ", mid)




