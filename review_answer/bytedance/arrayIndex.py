# coding=utf-8
# Time: 2020-01-19-11:27 
# Author: dongshichao

'''
插入一个整数到一个有序的数组中，并保证该数组是有序的
返回下标
'''

def insertArray(nums,A):
    if A<= nums[0]:
        return 0
    if A>=nums[-1]:
        return len(nums)
    # for i in range(1,len(nums)):
    #     if nums[i-1] <= A <= nums[i]:
    #         return i

    i,j=0,len(nums)-1
    while i <= j:
        mid = (j+i)//2
        if nums[mid] > A :
            j = mid-1
        elif nums[mid] < A:
            i = mid+1
        else:
            return mid
    return mid


print(insertArray([2,4,6,8,8,9,9,9,10],9))