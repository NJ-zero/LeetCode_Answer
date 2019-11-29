# coding=utf-8
# Time: 2019-11-26-19:39 
# Author: dongshichao
'''
287.寻找重复数

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3


二分法思路：
初试化左右 数字 边界left=1,right=n-1
循环条件left<right
mid=(left+right)//2
按照性质，统计数组中小于等于mid的元素个数count
若 count<=midc，说明重复数字一定在(mid,right](的范围内。令left=mid+1
若count>mid，说明重复数字一定在[left,mid]的范围内。令right=mid
返回left

'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                return i

    def finddd(self,nums):
        left = 1
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            count = 0
            for i in nums:
                if i <= mid:
                    count +=1
            if count <= mid:
                left = mid +1
            else:
                right=mid

        return left