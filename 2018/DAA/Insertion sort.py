'''
It is a comaprison based sorting technique. In this method, we first take an array and place the sorted elements in a sub array.
input: An array
output: Sorted array

#1 − If it is the first element, it is already sorted.
#2 − Pick next element
#3 − Compare with all elements in the sorted sub-list
#4 − Shift all the elements in the sorted sub-list that is greater than the value to be sorted
#5 − Insert the value
#6 − Repeat until list is sorted/ until last element of list has been reached

Psuedo code
for i <- 1 to n-1 do
	temp<-a[i]
	j<-i-1
	while j>=0 and temp<a[j] do
		a[j+1] <- a[j]
		a[j]<-temp
		j<-j-1
'''
import random
def insertionsort(list):
	len1=len(list)
	for i in range(0,len1):
		temp=list[i]
		j=i-1
		while(j>=0 and temp<list[j]):
			list[j+1]=list[j]
			list[j]=temp
			j=j-1
	print(list)
def random1():
	n=int(input("Enter n: "))
	list=[random.randint(0,10000) for i in range(0,n)]
	insertionsort()
random1()
