# coding=utf-8
# Time: 2019-11-15-17:13 
# Author: dongshichao
'''
238. 除自身以外数组的乘积

给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

思路：
先算一个数 左边的乘积
再算一个数 右边的乘积
两个乘积相乘 就是最终的结果
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        resl= [1] * n
        resr= [1] * n

        l,r=1,1
        for i in range(n):
            resl[i]=l
            l *= nums[i]
        for i in range(n)[::-1]:
            print(i)
            resr[i]=r
            r *= nums[i]

        res=[1] *n
        for i in range(n):
            res[i]=resl[i] * resr[i]
        return res

s=Solution()
print(s.productExceptSelf([1,2,3,4,5]))