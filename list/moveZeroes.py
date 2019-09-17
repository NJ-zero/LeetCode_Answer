# coding=utf-8
# Time: 2019-09-17-11:10 
# Author: dongshichao

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


思路：
要点是 要保持相对顺序
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        i=0
        for j in range(len(nums)):
            if nums[j] !=0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        return nums


if __name__=="__main__":
    s= Solution()
    print(s.moveZeroes([0,1,0,2,3]))
