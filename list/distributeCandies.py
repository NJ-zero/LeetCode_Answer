# coding=utf-8
# Time: 2019-12-19-17:12 
# Author: dongshichao
'''
575. 分糖果
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。
你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

示例 1:

输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多


'''
from collections import Counter
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = Counter(candies)
        m ,n = len(candies) , len(dic)

        if m >= n*2 :
            return n
        else:
            return m //2


s=Solution()
print(s.distributeCandies([1,1,2,3]))