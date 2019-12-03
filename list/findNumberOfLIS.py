# coding=utf-8
# Time: 2019-11-26-20:15 
# Author: dongshichao

'''
673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

思路：
对于每一个 j <i  且 nums[j] < nums[i]，都可以将nums[i] 加在以nums[j]结尾的最长子序列上
比较dp[j] +1 和 dp[i] 的大小
如果 比 dp[i] 长 ， 那么nums[i] 结尾的子序列长度 dp[j]+1,  count[i] = count[j]
如果 和 dp[i] 相等，那么说明这个长度已经找过一次， count[i] += count[j]

'''


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)      #记录第i个位置上结尾的，最长序列的长度
        counts = [1] * len(nums)    #记录具有该长度的序列的count

        for i ,num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        counts[i] = counts[j]
                    elif dp[j] + 1 == dp[i]:
                        counts[i] += counts[j]
        maxdp = max(dp)
        print(dp,counts)

        return sum(c for i ,c in enumerate(counts) if dp[i] == maxdp)


s=Solution()
print(s.findNumberOfLIS([1,3,5,4,7]))