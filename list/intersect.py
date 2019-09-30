# coding=utf-8
# Time: 2019-09-29-17:38 
# Author: dongshichao
'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count={}
        res=[]
        for i in nums1:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for i in nums2:
            if i in count and count[i] >0 :
                res.append(i)
                count[i] -=1
        return res

if __name__ == "__main__":
    s= Solution()
    print(s.intersect([1,4,6,8,3,5],[2,4,5,6,3]))