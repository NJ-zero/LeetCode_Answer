# coding=utf-8
# Time: 2019-10-16-11:36 
# Author: dongshichao

'''
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:

输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
示例 2:

输入:
nums = [1, 2, 3]
输出: -1
解释:
数组中不存在满足此条件的中心索引。

思路：
左右两边相等，等于 左边的和 乘以 2 加上中间数
'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = sum(nums)
        if len(nums) <=2 :
            return -1
        if sum(nums[1:])==0:
            return 0
        res1 = 0
        for i in range(1,len(nums)):
            res1 += nums[i-1]
            res2 = res - res1 - nums[i]
            print(i,res1,res2)
            if res2 == res1:
                return i
        return -1

    def ppp(self,nums):
        res = sum(nums)
        res1 = 0
        for i in range(len(nums)):
            if res1 *2 + nums[i] == res:
                return i
            res1 += nums[i]
        return -1


s= Solution()
print(s.pivotIndex([-1,-1,0,1,1,0]))
