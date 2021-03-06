# coding=utf-8
# Time: 2019-12-11-14:50 
# Author: dongshichao

'''
164. 最大间距
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

思路一：
先排序，在计算，时间复杂度 O(nlgn)

思路二：
 O(n) 的时间复杂度，这也就意味着普通排序这条路是走不通的。
用到桶排序
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            res = max(abs(nums[i]-nums[i-1]),res)
        return res

    def maxbucket(self, nums):
        import math
        n = len(nums)
        if len(nums)<2:
            return 0
        max_n = max(nums)
        min_n = min(nums)
        # 相邻的最大差值一定不小于该数组的最大值减去最小值除以间隔个数，取上界
        gap = math.ceil((max_n-min_n)/(len(nums)-1))

        # 这么多桶
        bucket = [[float("inf"),float("-inf")] for _ in range(n-1)]

        for num in nums:
            if num == max_n or num == min_n:   # 最大值、最小值不放到桶里面
                continue
            loc = (num - min_n) //gap     # 决定这个数放在哪个桶，也就是距离最小数有几个gap
            bucket[loc][0] = min(num,bucket[loc][0])
            bucket[loc][1] = max(num,bucket[loc][1])

        premin = min_n
        res = float("-inf")
        for x,y in bucket:
            if x == float("inf"):
                continue
            res = max(res,x-premin)
            premin = y
        res = max(res,max_n-premin)

        return res

s=Solution()
print(s.maximumGap([3,6,9,1]))
print(s.maxbucket([3,6,9,1]))

a=[9,10,11,25]
s={1:0,2:0,3:0}
for ass in a:
    print("ass:",ass)
    s = dict(sorted(s.items(),key = lambda x:x[1]))

    for i in s :
        if s[i] < ass:
            s[i] = ass
            break
    print(s)

print(list(s.values()))