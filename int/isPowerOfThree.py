# coding=utf-8
# Time: 2019-09-17-19:58 
# Author: dongshichao

'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true

由于输入是int，正数范围是0-2^31，
在此范围中允许的最大的3的次方数为3^19=1162261467，那么我们只要看这个数能否被n整除即可
'''



class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        for i in range(n):
            if 3**i ==n :
                return True
            elif 3**i >n:
                return False

        return False

    def isPower3(self,n):
        return n >0 and 3**19 % n ==0


if __name__ =="__main__":
    s =Solution()
    print(s.isPowerOfThree(29))