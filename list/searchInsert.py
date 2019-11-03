# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/10/8

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if nums[-1]<target:
            return len(nums)
        elif nums[0]>target:
            return 0
        else:
            if target in nums:
                return nums.index(target)
            else:
                for i in range(len(nums)):
                    if nums[i]<target and nums[i+1]>target:
                        return i+1
    def searchInnnn(self,nums,target):
        if nums[-1] < target:
            return len(nums)
        elif nums[0] >= target :
            return 0
        else:
            for i in range(1,len(nums)):
                if nums[i] == target:
                    return i
                else:
                    if nums[i-1] < target < nums[i]:
                        return i

if __name__ == "__main__":
    s = Solution()
    a=s.searchInnnn([1,3,5,6],5)
    print(a)