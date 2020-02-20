# coding=utf-8
# Time: 2020-01-17-19:44 
# Author: dongshichao

'''
一个数据相邻元素之差，求最大者
'''

def maxgap(nums):
    res = 0
    for i in range(1,len(nums)):
        res = max(abs(nums[i]-nums[i-1]),res)
    return res

print(maxgap([1,3,5,6,8,13,1]))