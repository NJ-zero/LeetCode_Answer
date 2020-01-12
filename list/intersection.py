# coding=utf-8
# Time: 2019-10-30-16:34 
# Author: dongshichao

'''
349.两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。


'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count={}
        res=[]
        for i in nums1:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        for i in nums2:
            if i in count and count[i] > 0:
                res.append(i)
                count[i] -=1

        return list(set(res))
