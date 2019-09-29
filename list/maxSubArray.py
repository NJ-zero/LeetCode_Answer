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

    def maxsub(self,nums):
        res = 0
        maxnum = nums[0]
        for i in range(len(nums)):
            res += nums[i]
            maxnum = max(maxnum,res)

            if res < 0 :
                res = 0
        return maxnum

    def maxsub3(self,nums):
        '''
        设sum[i]为以第i个元素结尾的最大的连续子数组的和
        那么以第i个元素结尾且和最大的连续子数组实际上，
        要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，要么是只包含第i个元素，即sum[i]= max(sum[i-1] + a[i], a[i])

        :param nums:
        :return:
        '''
        n = len(nums)
        for i in range(1,n):
            submax = max(nums[i],nums[i-1]+nums[i])
            nums[i] = submax
        return max(nums)


if __name__=="__main__":
    s=Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxsub([-2,1,4,6,-9,10]))