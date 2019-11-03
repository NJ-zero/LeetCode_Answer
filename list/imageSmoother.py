# coding=utf-8
# Time: 2019-10-14-10:55 
# Author: dongshichao

'''
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0


'''

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m = len(M),len(M[0])
        res=[]
        for i in range(n):
            s=[]
            for j in range(m):
                nn=[i-1,i,i+1]
                mm=[j-1,j,j+1]
                count=0
                summ=0
                for i_n in nn:
                    for j_m in mm:
                        if 0 <= i_n <= n-1 :
                            if 0 <= j_m <= m-1:
                                count += 1
                                summ += M[i_n][j_m]
                s.append(summ//count)
            res.append(s)
        return res

s=Solution()
print(s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
