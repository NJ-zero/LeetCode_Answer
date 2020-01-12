# coding=utf-8
# Time: 2019-12-09-20:03 
# Author: dongshichao

'''
977.有序数组的平方

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。


示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]


'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A[0] >=0:
            return [i**2 for i in A]
        if A[-1] <=0:
            return [i**2 for i in A][::-1]

        A=[i**2 for i in A]
        A.sort()
        return A



S=Solution()
print(S.sortedSquares([-9,-3,-1,1,4,5]))
