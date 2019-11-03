# coding=utf-8
# Time: 2019-10-30-19:15 
# Author: dongshichao
'''
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。


二分法找边界
'''


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,h =1 ,n
        if isBadVersion(1) :
            return 1
        mid = (l+h)//2
        while l < h :
            if isBadVersion(mid):
                h = mid
            else:
                l = mid+1
            mid = (l+h)//2
        return l