# coding=utf-8
# Time: 2019-11-18-20:04 
# Author: dongshichao
'''
78。子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

思路：
迭代的方法：
第一个 【】
第二轮 【】【1】
第三轮 【】【1】【2】【1，2】
第三轮 【】【1】【2】【1，2】【3】【1，3】【2，3】【1，2，3】
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for num in nums:
            res = res + [[num]+i for i in res]
            # print(res)
        return res

    def subsss(self,nums):
        res=[]
        n=len(nums)

        def help(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                help(j+1,tmp+[nums[j]])

        help(0,[])
        return res

s=Solution()
print(s.subsets([1,2,3]))

print(s.subsss([1,2,3]))