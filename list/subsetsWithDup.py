# coding=utf-8
# Time: 2019-11-19-11:02 
# Author: dongshichao

'''
90.子集II

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n = len(nums)
        if not nums:
            return res
        nums.sort()
        def help(idx,tmp):
            res.append(tmp)
            for i in range(idx,n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                help(i+1,tmp+[nums[i]])

        help(0,[])
        return res



s=Solution()
print(s.subsetsWithDup([1,2,2]))
