# coding=utf-8 
# @Time    : 2020/4/7 8:06 下午
# @Author  : 'Shichao-Dong'


'''
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
1.延对角线 交换
在反转每一个子数组

2.matrix[i][j] ---> new_matrix[j][n-i-1]

'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix=[[]]*n
        for i in range(n):
            new_matrix[i] = [ _ for _ in range(n)]
        # new_matrix = [[ _ for _ in range(n)]]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n-i-1] = matrix[i][j]
        return (new_matrix)


s=Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
