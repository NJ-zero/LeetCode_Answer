# coding=utf-8
# Time: 2019-10-30-11:34 
# Author: dongshichao

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。


'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=len(nums1)+len(nums2)
        if n % 2 ==1:
            return self.finek(nums1,nums2,n//2)
        else:
            return (self.finek(nums1,nums2,n//2)+self.finek(nums1,nums2,n//2-1))//2



    def finek(self,nums1,nums2,k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        i,j = len(nums1)//2,len(nums2)//2

        m1,m2 = nums1[i],nums2[j]
        if i +j <k:
            if m1>m2:
                self.finek(nums1,nums2[j+1],k-j-1)
            else:
                self.finek(nums1[i+1:],nums2,k-i-1)
        else:
            if m1 > m2:
                self.finek(nums1[:i],nums2,k)
            else:
                self.finek(nums1,nums2[:j],k)