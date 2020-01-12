# coding=utf-8
# Time: 2019-12-16-17:11 
# Author: dongshichao

'''
47.全排列 II

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

和46 全排列 一样


'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def helper(nums):
            if len(nums) <=1:
                return [nums]
            n = []
            for i in range(len(nums)):
                if i >0 and nums[i] == nums[i-1]:
                    continue
                iterm = nums.pop(i)
                subres = helper(nums)
                for res in subres:
                    n.append([iterm] + res)
                nums.insert(i,iterm)
            return n

        res = helper(nums)
        return res