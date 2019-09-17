# coding=utf-8
# Time: 2019-09-17-16:23 
# Author: dongshichao

'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

解题思路：

'''



class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in count:
            if count[i] > len(nums)//2:
                return i

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,2,3,4,2,2,2,2,2,2]))