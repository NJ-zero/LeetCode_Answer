# coding=utf-8
# Time: 2019-11-12-20:16 
# Author: dongshichao

'''
128.最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

思路：
去重后排序
res=1
后一个比前一个大1 ，则tmp+=1
res= max(res,tmp)
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        i,j=0,len(nums)-1
        res=1
        while i < j:
            tmp=1
            while i <j and nums[i] == nums[i+1]-1:
                tmp +=1
                i+=1

            res = max(res,tmp)
            i+=1

        return res