# coding=utf-8
# Time: 2019-10-30-20:50 
# Author: dongshichao

'''
718.最长重复子数组

给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。


'''

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lenA = len(A)
        lenB = len(B)
        mat = [[0]*(lenB+1) for _ in range(lenA+1)]
        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                if A[i-1]==B[j-1]:
                    mat[i][j]=mat[i-1][j-1]+1
        return max([max(line) for line in mat])
