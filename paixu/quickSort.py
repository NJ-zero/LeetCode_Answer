# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/21 

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        p=arr[0]
        less=[i for i in arr[1:] if i <= p]
        more=[i for i in arr[1:] if i>p]
        return quicksort(less)+ [p] +quicksort(more)

a=[2,1,4,5,12,41,62,13,18,23,25]
newa=quicksort(a)
print(newa)

def sort(arr,first,last):
    if first<last:
        i=first
        j=last

        base=arr[i]
        while (i<j):
            if arr[j] >= base:
                j=j-1
            arr[i]=arr[j]

            if arr[i]< base:
                i=i+1
            arr[j]=arr[i]
        arr[i]=base
        sort(arr,first,i-1)
        sort(arr,j+1,last)
    return arr

b=[2,1,4,5,12,41,62,13,18,23,25]
newa=sort(b,0,len(b)-1)
print(newa)