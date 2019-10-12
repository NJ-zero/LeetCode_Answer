# coding=utf-8
# Time: 2019-10-12-10:52 
# Author: dongshichao

'''
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

解题思路：
我们可以使用一个宽度为3的滑窗，这里通过指针i表示滑窗中心，则滑窗中包含3个元素[i-1, i, i+1]，
指针i从第二个元素开始遍历到倒数第二个元素，在遍历的过程中，我们查看滑窗中是否所有位置都没有种花，
如果没有，那么我们在滑窗中心栽一朵，否则继续遍历，如果手头没有剩下花了，说明可以栽下那么多，否则不能。
这里需要注意的是，我们要考虑两端的情况，需要将数组做padding（左右各增加一个0）
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed) -1 ):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] ==0:
                flowerbed[i] = 1
                n -=1
            if n <= 0:
                return True
        return False

s = Solution()
print(s.canPlaceFlowers([1,0,0,1],1))