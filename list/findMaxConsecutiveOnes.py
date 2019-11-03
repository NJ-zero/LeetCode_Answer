# coding=utf-8
# Time: 2019-10-10-15:38 
# Author: dongshichao


'''
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.


'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res=[]
        for i in nums:
            if i == 1:
                sum +=1
            else:
                res.append(sum)
                sum = 0
            res.append(sum)
        return max(res)
    def findMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res=0
        for i in nums:
            if i == 1:
                sum +=1
            else:
                res= max(res,sum)
                sum = 0
            res=max(res,sum)
        return (res)

s=Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,0,0]))
print(s.findMax([1,1,0,1,1,1,0,1,0,0]))