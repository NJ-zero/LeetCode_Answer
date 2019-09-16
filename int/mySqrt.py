# coding=utf-8
# Time: 2019-09-07-15:00 
# Author: dongshichao


'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

'''




class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <=3 :
            return 1
        i=1
        j=x
        while i <=j:
            mid = (i+j)//2

            s = mid **2

            if s <=x < (mid+1)**2:
                return mid
            if s > x:
                j =mid
            if s < x:
                i=mid


if __name__=="__main__":
    s = Solution()
    print(s.mySqrt(36))