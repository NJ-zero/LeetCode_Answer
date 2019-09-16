# coding=utf-8
# Time: 2019-09-16-16:56 
# Author: dongshichao
'''
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 
示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.

思路：
1。递归
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2)


'''


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <=1 :
            return N
        else:
            return self.fib(N-1)+self.fib(N-2)

    def fib2(self, N):
        res=[0,1,1]
        if N <=1:
            return N
        for i in range(2,N+1):
            res.append(res[i-1]+res[i-2])

        return res[-1]

if __name__ == "__main__":
    s=Solution()

    print(s.fib2(4))


