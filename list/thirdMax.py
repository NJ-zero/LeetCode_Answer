# coding=utf-8
# Time: 2019-10-10-11:23 
# Author: dongshichao

'''
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .


'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            res.sort()
            if len(res)>3:
                res = res[-3:]
        if len(res)==3 :
            return res[0]
        else:
            return res[-1]

    def thirdMaxxxx(self,nums):
        res = [float("-inf")]*3
        for i in nums:
            if i in res:
                continue
            if i > res[0]:
                res = [i, res[0], res[1]]
            elif i > res[1]:
                res = [res[0], i, res[1]]
            elif i > res[2]:
                res = [res[0], res[1], i]
            print(res)
            return res[-1] if res[2] != float("-inf") else res[0]



s=Solution()
print(s.thirdMax([5,2,4,1,3,6,0]))
print(s.thirdMaxxxx([5,2,4,1,3,6,0]))
