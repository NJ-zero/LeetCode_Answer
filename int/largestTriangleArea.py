# coding=utf-8
# Time: 2019-11-08-11:05 
# Author: dongshichao

'''
812. 最大三角形面积
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2

纯数学运算：
三角形的三个顶点坐标求其面积的公式为:
S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
'''

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """


s=Solution()
print(s.largestTriangleArea([[4,6],[6,5],[3,1]]))