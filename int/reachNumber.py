# coding=utf-8
# Time: 2019-11-08-10:29 
# Author: dongshichao
'''
754.到达终点数字

在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。

示例 1:

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
示例 2:

输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。

思路：
先取绝对值
当走的距离等于target时返回
当走的距离大于target,如果distance-target 差为 偶数
即说明 中间一个数 倒退即可
因为 倒退就是 减去该数的两倍
1-2+3=2
1+2+3=6
6-2=4=2*2

'''

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        n= abs(target)
        num,distance = 0,0
        while True:
            if distance >=n and (distance-n)%2 == 0:
                return num
            num +=1
            distance += num

s=Solution()
print(s.reachNumber(5))


