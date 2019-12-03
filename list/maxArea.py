# coding=utf-8
# Time: 2019-11-05-20:06 
# Author: dongshichao

'''
11. 盛最多水的容器

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

思路：
双指针
首位两个指针 i j

s= j-i * min(s[j],s[i])

'''

class Solution(object):
    def maxArea(self, s):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0 , len(s)-1
        res =0
        while i < j:
            res = max(res,min(s[i],s[j])*(j-i))
            if s[i] < s[j]:
                i+=1
            else:
                j-=1
        return res

    def mmmm(self,s):
        '''
        暴力解法，时间复杂度O(n^2)
        :param s:
        :return:
        '''
        res=0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                res = max(res, min(s[i], s[j]) * (j - i))
        return res


s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.mmmm([1,8,6,2,5,4,8,3,7]))