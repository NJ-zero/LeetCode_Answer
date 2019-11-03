# coding=utf-8
# Time: 2019-10-10-16:02 
# Author: dongshichao

'''
给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

示例 1:

输入: [3, 1, 4, 1, 5], k = 2
输出: 2
解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。


'''


class Solution(object):
    def findPairs(self, nums, k):
        """
        暴力解法，会导致超时
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=[]
        len_num = len(nums)
        for i in range(len_num - 1):
            for j in range(i+1,len_num):
                if abs(nums[j]-nums[i]) == k:
                    n=[min(nums[i],nums[j]),max(nums[i],nums[j])]
                    print(n)
                    if n not in res:
                        res.append(n)
        print(len(res))

    def findPPP(self,nums,k):
        dic={}
        count = 0
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        if k < 0 :
            return 0
        if k == 0:
            for i in dic.keys():
                if dic[i] > 1:
                    count +=1
            return count
        if k >0 :
            for i in dic.keys():
                if i + k in dic:
                    count +=1
            return count

s= Solution()
s.findPairs([1,3,1,5,3],0)
print(s.findPPP([1,3,1,5,3],0))