# coding=utf-8
# Time: 2019-11-21-16:32 
# Author: dongshichao


'''
560.和为k的子数组

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。


思路：
借助哈希表保存累加和sumsum及出现的次数。若累加和sum-k在哈希表中存在，则说明存在连续序列使得和为k。
也就是说： x+k=sum  x sum 均在hash中，那么 sum-k =x 出现的次数就是 可能为k的次数
比如
1 3 5 8 9 11  k=6
3+6=9
5+6=11
则 3的value + 5的value 就是 和为6 的子序列 和
则之前的累加和中，sum-k出现的次数即为有多少种子序列使得累加和为sum-k。

哈希
初始化哈希表hash=\{0:1\}hash={0:1}，表示累加和为0，出现了1次。初始化累加和sum=0。初始化结果count=0

遍历数组：

更新累加和sum+=nums[i]sum+=nums[i]
若sum-ksum−k存在于hashhash中，说明存在连续序列使得和为kk。
则令count+=hash[sum-k]count+=hash[sum−k]，表示sum-ksum−k出现几次，就存在几种子序列使得和为kk。
若sumsum存在于hashhash中，将其出现次数加一。若不存在，将其加入hashhash
返回countcount


'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if not nums:
            return 0
        if min(nums) > k:
            return 0

        hash={0:1}     #总和为0，出现了1次
        sum=0
        count=0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum-k in hash):
                count += hash[sum-k]
            if sum in hash:
                hash[sum] +=1
            else:
                hash[sum] = 1
        return count


s=Solution()
print(s.subarraySum([1,1,1],2))