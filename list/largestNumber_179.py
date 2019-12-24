# coding=utf-8
# Time: 2019-12-24-15:34 
# Author: dongshichao

'''
179. 最大数

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        s = ""
        if nums[-1] == 0 :
            return ("0")
        for i in nums:
            s = str(i) + s
        return s

s= Solution()
print(s.largestNumber([12,23,45,234]))