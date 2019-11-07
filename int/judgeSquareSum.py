# coding=utf-8
# Time: 2019-11-07-19:30 
# Author: dongshichao

'''
633.平方数之和

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
 

示例2:

输入: 3
输出: False

'''

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i,j=0,int(c**0.5)
        while i <=j:
            if i**2 + j**2 == c:
                return True
            elif i**2 + j**2 < c:
                i+=1
            else:
                j-=1
        return False

s=Solution()
print(s.judgeSquareSum(10))