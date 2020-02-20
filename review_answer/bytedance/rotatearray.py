# coding=utf-8
# Time: 2020-01-16-14:51 
# Author: dongshichao
'''
旋转数组

[1,2,3,4,5] -- 2
[4,5,1,2,3]
'''

def rotate(nums,k):
    if len(nums) <=1:
        return nums
    n = len(nums)
    k = k % n
    print(k)
    nums[:] = nums[n-k:]+nums[:n-k]
    return nums

print(rotate([1,2,3,4,5,6],2))