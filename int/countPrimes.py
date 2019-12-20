# coding=utf-8
# Time: 2019-12-19-17:44 
# Author: dongshichao

'''
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

class Solution(object):
    def countPrimes(self, n):
        """
        暴力解法,会超时
        :type n: int
        :rtype: int
        """
        res= 0
        if n <= 2:
            return res
        for i in range(2,n+1):
            for j in range(2,int(i**0.5)+1):
                if i % j ==0:
                    break
            else:
                res +=1
        return res
    def cooo(self,n):
        isp=[1] * n
        res = 0
        for i in range(2,n):
            if isp[i] == 1:
                res +=1
            j=i
            while i * j < n:
                isp[i*j] = 0
                j+=1
        return res


s=Solution()
print(s.countPrimes(10))