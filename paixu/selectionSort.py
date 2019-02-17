# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/16 

def selectsort(a):
    for i in range(len(a)-1):
        min=a[i]
        for j in range(i+1,len(a)):
            if (min > a[j]):
                tmp = a[j]
                a[j]=min
                min =tmp
        a[i]=min
    print(a)
a=[2,1,3,5,12,15,34,23]
selectsort(a)


def find(arr):
    for i in range(len(arr)-1):
        small=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<small:
                tmp=small
                small=arr[j]
                arr[j]=tmp
        arr[i]=small
    print(arr)

find([1,333,5,12,14,23,24,36,11,10,9])