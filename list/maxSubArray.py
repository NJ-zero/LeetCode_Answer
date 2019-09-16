# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/7 
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        l_nums=len(nums)
        count=nums[0]

        for i in range(l_nums):
            sum+=nums[i]
            if sum>count:
                count=sum
            if sum<0:
                sum=0
        return count

if __name__=="__main__":
    s=Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))