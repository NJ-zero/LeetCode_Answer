# coding=utf-8
# Time: 2019-10-12-17:04 
# Author: dongshichao

'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


解题思路：
一个为K的滑窗，计算滑窗内的sum ，先计算好，前K个元素的和 （每次都单独计算会超时）
然后对比滑窗前后的大小，如果大，就加上差额
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n == k :
            return  sum(nums)/float(k)
        s = 0
        for i in range(k):
            s += nums[i]
        res = s
        for i in range(1,n-k+1):
            res += nums[i+k-1] - nums[i-1]
            if res > s:
                s = res

        return s/float(k)

s= Solution()
print(s.findMaxAverage([0,4,0,3,2], 1))