# coding=utf-8
# Time: 2019-09-30-09:50 
# Author: dongshichao

'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

解题思路：
从数学的角度，0-n,确定会缺失一个数字
将数组求和，和0-n求和，差额就是少的数字
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1=0
        for i in nums:
            s1 += i
        s2 = (len(nums)+1)*len(nums)//2
        return s2-s1

if __name__=="__main__":
    s= Solution()
    print(s.missingNumber([1,3,5,0,2]))