# coding=utf-8
# Time: 2019-12-18-17:12 
# Author: dongshichao

'''
447.回旋镖的数量
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:
输入:
[[0,0],[1,0],[2,0]]
输出:
2
解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]


思路：
借助hash表
遍历points,每个数 作为 i 点时 维护一个空的hash表 freq ,key 为 距离，value 为 值
排列组合 v * v-1

'''


class Solution:
    def dis(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def numberOfBoomerangs(self, points):
        res = 0
        for i in points:
            freqmap={}
            for j in points:
                if j !=i:
                    d = self.dis(i,j)
                    freqmap[d] = freqmap[d] + 1 if d in freqmap else 1
            for v in freqmap.values():
                res += v * (v-1)

        return res



