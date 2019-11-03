# coding=utf-8
# Time: 2019-10-30-19:24 
# Author: dongshichao

'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False


'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,h = 1,num
        while l <= h:
            mid = (l+h)//2
            print(mid)
            if mid ** 2 == num:
                return True
            elif mid **2 < num:
                l=mid+1
            else:
                h=mid-1
        return False

s=Solution()
print(s.isPerfectSquare(1))