# coding=utf-8
# Time: 2019-09-17-17:00 
# Author: dongshichao

'''
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

解题思路：
在末尾形成0来自于因子 2 * 5，只要有 5 ，一定有 0
n = 5  拆出 1 个
n = 10 拆出 2 个

n = 25 拆出 6 个,因为 25 自身 能多拆一个

相当于 n/5 + n/25 + n/125 ...
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >0 :
            res += n//5
            n //= 5
        return res

if __name__=="__main__":
    s =Solution()
    print(s.trailingZeroes(31))