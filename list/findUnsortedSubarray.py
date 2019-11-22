# coding=utf-8
# Time: 2019-10-11-17:25 
# Author: dongshichao

'''
581. 最短无序连续子数组

给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。


'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        if nums == sorted(nums):
            return 0

        i,j = 0,len(nums)-1
        n = sorted(nums)
        while i < j :
            if nums[i] == n[i]:
                i +=1
                continue
            if nums[j] == n[j]:
                j -=1
                continue
            return j -i +1

    def fff(self,nums):
        if len(nums) == 1:
            return 0
        maxval,minval = nums[0] ,nums[-1]
        j,k,n =-1, 0 ,len(nums)
        for i in range(n):
            maxval = max(maxval,nums[i])
            if nums[i] < maxval:
                j = i
            minval = min(minval,nums[n-i-1])
            if nums[n-i-1] > minval:
                k = n-i-1
        return j-k+1

    def ffff(self,nums):
        '''
        两次遍历，一次从前往后，一次从后往前
        :param nums:
        :return:
        '''
        n = len(nums)
        if n <=1:
            return 0

        maxval,minval = nums[0] ,nums[-1]
        right=0
        for i in range(n):
            if nums[i] >= maxval:
                maxval = nums[i]
            else:
                right=i
        left=n
        for i in range(n)[::-1]:
            if nums[i] <= minval:
                minval = nums[i]
            else:
                left=i

        return right-left+1


s =Solution()
print(s.findUnsortedSubarray([1,3,2,3,3]))
print(s.fff([1,3,2,3,3]))
