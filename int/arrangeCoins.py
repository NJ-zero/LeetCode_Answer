# coding=utf-8
# Time: 2019-10-30-16:49 
# Author: dongshichao
'''
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.


'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            if (i+1)*i/2 <=n and (i+1)*(i+2)/2 >n:
                return i

    def erfe(self,n):
        l=0
        h=n
        while l <=h:
            mid = (l+h)//2
            sum = mid*(mid+1)//2
            sum2=(mid+1)*(mid+2)//2
            print(l,h,sum)
            if sum <=n <sum2:
                return mid
            elif sum < n:
                l= mid+1
            else:
                h = mid -1
        return l

s=Solution()
print(s.arrangeCoins(9))
print(s.erfe(0))