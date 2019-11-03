# coding=utf-8
# Time: 2019-11-01-15:28 
# Author: dongshichao

'''
852. 山脉数组的峰顶索引

我们把符合下列属性的数组 A 称作山脉：

A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

 
示例 1：

输入：[0,1,0]
输出：1
示例 2：

输入：[0,2,1,0]
输出：1


'''

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l,r = 0 , len(A)-1
        while l <= r:
            mid = l+(r-l)//2
            if A[mid]>A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid+1]>A[mid]>A[mid-1]:
                l=mid+1
            elif A[mid-1]>A[mid]>A[mid+1]:
                r = mid-1

s=Solution()
print(s.peakIndexInMountainArray([0,1,2,1]))


