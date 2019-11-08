# coding=utf-8
# Time: 2019-11-08-14:20 
# Author: dongshichao
'''
1175.质数排列

请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。

思路：
统计x个质数，y个非质数
结果为 x的阶乘 * y的阶乘

'''

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(i):
            for num in range(2,i):
                if (i % num) == 0:
                    return False
            return True

        if n ==1 :
            return 1

        c=0
        for i in range(2,n+1):
            if check(i):
                c +=1
        s=n-c

        res=1
        for i in range(1,c+1):
            res *=i
        for i in range(1,s+1):
            res *=i
        return res%(10**9 + 7)

s=Solution()
print(s.numPrimeArrangements(100))