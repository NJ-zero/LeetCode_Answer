# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/28
'''
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
输入: [1,2,3,4]
输出: 24
注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        a = nums[0]*nums[1]*nums[-1]
        b = nums[-1]*nums[-2]*nums[-3]
        if a>b :
            return a
        else:
            return b