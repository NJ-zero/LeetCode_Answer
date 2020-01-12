# coding=utf-8
# Time: 2019-12-05-19:49 
# Author: dongshichao

'''
159. 至多包含两个不同字符的最长子串

给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

思路：
1。初始，left指针和right指针都指向S的第一个元素.
2。将 right 指针右移，扩张窗口，直到得到一个可行窗口，即 包含3个不同的元素
3。将left指针逐个右移，知道包含 2 个不同的元素
4。重复第二步
'''
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) :
        lookup = defaultdict(int)
        i,j = 0,0
        max_len,counter = 0,0
        while j < len(s):
            if lookup[s[j]] == 0:
                counter +=1   #统计滑窗中的不同元素个数
            lookup[s[j]] +=1
            j+=1

            while counter > 2:
                if lookup[s[i]] ==1:
                    counter -=1
                lookup[s[i]] -=1
                i +=1
            max_len = max(j-i,max_len)
        return max_len

s=Solution()
print(s.lengthOfLongestSubstringTwoDistinct("abcdde"))


