# coding=utf-8
# Time: 2020-02-20-15:05 
# Author: dongshichao
'''

一个数组，找到满足 i< j ,nums[j]-nums[i] 的最大值
'''

def maxji(nums):
    min_num=nums[0]
    res=nums[1]-nums[0]
    for i in range(len(nums)):
        min_num = min(nums[i],min_num)
        res = max(res,nums[i]-min_num)
    return res


res=maxji([2,5,8,1,18])
print(res)