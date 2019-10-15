# coding=utf-8
# Time: 2019-10-15-15:06 
# Author: dongshichao
'''
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6


'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        print(dic)
        ss=(max([dic[i] for i in dic]))
        if ss == 1:
            return 1
        items=[]
        for i in dic:
            if dic[i] == ss:
                items.append(i)
        res = len(nums)
        for item in items:
            i,j = 0 ,len(nums)-1
            while i <j :
                if nums[i] != item:
                    i+=1
                    continue
                if nums[j] != item:
                    j -=1
                    continue
                break
            res = min(res,j-i+1)
        print(res)

s = Solution()
print(s.findShortestSubArray([1,1,1,2,1,2,4,3,2,2,2,1]))