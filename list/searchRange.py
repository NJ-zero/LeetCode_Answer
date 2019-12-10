# coding=utf-8
# Time: 2019-12-10-14:00 
# Author: dongshichao

'''
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

思路：
1.线性查，时间复杂度O(n)

2.二分查找 时间复杂福O(log n)
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_1,index_2 = -1,-1

        for i in range(len(nums)):
            if nums[i] == target:
                index_1 = i
                break

        for j in range(len(nums))[::-1]:
            if nums[j] == target:
                index_2 = j
                break
        return [index_1,index_2]






