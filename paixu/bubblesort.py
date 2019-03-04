# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/4

def bubblesort(n):
    '''
    :param n: list
    :return:
    '''
    l=len(n)
    for i in range(l):
        for j in range(l-1):
            if n[j+1]<n[j]:
                n[j],n[j+1]=n[j+1],n[j]
    return n

n=[2,5,4,9,6,12,45,23,155,1,75]
print(bubblesort(n))