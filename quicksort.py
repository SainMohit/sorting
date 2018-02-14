n = int(input("enter the no of element in list ") )
lis= []
for i in range (0,n):
    lis.append(int(input("enter {0}th element " .format(i+1))))

def quicksort(low,high):
    if(low<high):
	pi = partition(low,high)
	quicksort(low,pi-1)
	quicksort(pi+1,high)


def partition(low,high):
    x = lis[high]
    j=low-1
    for i in range(low,high):
	if(lis[i]<x):
	    j = j+1
	    lis[i],lis[j] = lis[j],lis[i]
	    
    lis[j+1],lis[high]=lis[high],lis[j+1] 
   
   
    return j+1 
      


quicksort(0,n-1)
print(lis)


