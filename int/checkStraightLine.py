# coding=utf-8
# Time: 2019-11-11-19:04 
# Author: dongshichao
'''
1232. 缀点成线

在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，
其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。


'''

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        n = len(coordinates)
        if n <=1:
            return False
        s=[x[0] for x in coordinates]
        if len(set(s))==1:
            return True

        x1,y1,x2,y2=coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1]
        if x1==x2:
            return False
        k=(y1-y2)/(x1-x2)

        for i in range(1,n):
            x3,y3=coordinates[i][0],coordinates[i][1]
            if x1==x3:
                return False
            print((y1-y3)/(x1-x3))
            if (y1-y3)/(x1-x3) != k:
                print((y1-y3)/(x1-x3))
                return False
        return True

s=Solution()
print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))