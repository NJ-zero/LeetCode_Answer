# coding=utf-8
# Time: 2019-11-09-11:24 
# Author: dongshichao
'''
1217.玩筹码

数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。

你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：

将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
最开始的时候，同一位置上也可能放着两个或者更多的筹码。

返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。


示例 1：
输入：chips = [1,2,3]
输出：1
解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。

思路：
求奇数偶数个数，返回较小的那个

'''

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        n=len(chips)
        o=[i for i in chips if i%2==0]
        j=[i for i in chips if i%2!=0]
        print(o,j,len(o),len(j))
        return min(len(o),len(j))

s=Solution()
print(s.minCostToMoveChips([2,2,2,3,3]))