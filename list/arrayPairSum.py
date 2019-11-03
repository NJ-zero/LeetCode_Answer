# coding=utf-8
# Time: 2019-10-11-10:51 
# Author: dongshichao

'''
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).

解题思路：
排序后，去 0 2 4 6..上面的元素，求和
'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        sum =0
        for i ,v in enumerate(nums):
            if i % 2 ==0:
                sum += v
        return sum

s= Solution()
print(s.arrayPairSum([1,4,3,2]))


