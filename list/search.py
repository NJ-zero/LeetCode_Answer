# coding=utf-8
# Time: 2019-11-15-19:14 
# Author: dongshichao

'''
33. 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1


时间复杂度要求
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l <r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l=mid+1
            else:
                r=mid
        pol = l
        ans = self.binary_search(nums[:pol],target)

        if ans == -1:
            ans = self.binary_search(nums[pol:],target)
            if ans != -1:
                ans +=len(nums[:pol])

        return ans



    def binary_search(self,nums,target):
        index=-1
        l=0
        r=len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid -1
            else:
                index = mid
                break
        return index




    def seeee(self,nums,target):
        return  nums.index(target) if target in nums else -1

