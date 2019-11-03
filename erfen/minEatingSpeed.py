# coding=utf-8
# Time: 2019-11-01-16:08 
# Author: dongshichao

'''
875. 爱吃香蕉的珂珂

珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。
每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。


思路：
如果总和比 H 小，则返回 1

假设综合 sum / H =m ，每小时至少吃 m 个（每一堆正好能被整除）
所以 速度 最小是 m
不能被整除的情况：
(x-1)//m +1  for x in piles
sum 》 H
要不然 m+=1

'''



class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        piles.sort()
        if len(piles)  == H:
            return piles[-1]
        if sum(piles) // H ==0:
            return 1
        m=sum(piles)//H

        while sum([(x-1)//m +1 for x in piles]) > H:
            m +=1
        return m

s=Solution()
print(s.minEatingSpeed([3,6,7,11],8))