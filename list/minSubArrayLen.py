# coding=utf-8
# Time: 2019-08-13-16:49 
# Author: dongshichao

'''
209. 长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

要求是连续子数组，所以我们必须定义 i，j两个指针，i 向前遍历，j 向后遍历，
相当与一个滑块，这样所有的子数组都会在 [i...j] 中出现，如果 nums[i..j] 的和小于目标值 s，那么j向后移一位，
再次比较，直到大于目标值 s 之后，i 向前移动一位，缩小数组的长度。
遍历到i到数组的最末端，就算结束了，如果不存在符合条件的就返回 0。

'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i , j = 0 ,0
        sum = 0
        res = len(nums)+1
        while j < len(nums):
            sum += nums[j]
            while sum >=s:
                res = min(res,j-i+1)
                sum -= nums[i]
                i +=1
            j+=1
        if res == len(nums)+1:
            res = 0
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
