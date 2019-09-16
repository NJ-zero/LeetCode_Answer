# coding=utf-8
# Time: 2019-09-16-16:33 
# Author: dongshichao

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

思路：
最简单的是递归
s[n] = s[n-1]+s[n-2],但是递归耗时过长，容易栈溢出

维护一个数组来记录每个答案
[1,1]
0 和 1时，答案为1
后续满足 s[n] = s[n-1]+s[n-2]
append到数组里

'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        for i in range(2, n + 1):
            res.append(res[i - 1] + res[i - 2])
        return res[n]

    def climbdigui(self,n):
        if n ==1 or n ==0:
            return 1
        else:
            return self.climbdigui(n-1)+self.climbdigui(n-2)


if __name__ =="__main__":
    s = Solution()
    print(s.climbStairs(8))