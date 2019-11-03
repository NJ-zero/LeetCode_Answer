# coding=utf-8
# Time: 2019-10-09-14:39 
# Author: dongshichao

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。

思路：
在价格最低的时候买入，差价最大的时候卖出就解决了

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        二次循环，会导致超时
        :type prices: List[int]
        :rtype: int
        """
        res=[]
        if len(prices) <=1:
            return 0
        for i in range(len(prices)):
            j=i
            sum=0
            while j < len(prices):
                sum = max(sum,prices[j]-prices[i])
                j+=1
            res.append(sum)
        return max(res)

    def maxpppp(self,prices):
        if len(prices) <=1:
            return 0
        pp=0
        minnum = prices[0]
        for j in prices:
            minnum = min(minnum,j)
            pp = max(j-minnum,pp)
            print(minnum,pp)
        return pp

if __name__ == "__main__":
    s =Solution()
    print(s.maxpppp([7,1,5,3,6,4]))
