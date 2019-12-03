# coding=utf-8
# Time: 2019-11-21-14:36 
# Author: dongshichao

'''
5.最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

思路：
中心扩散
注意考虑 aba  aa  均为 有效回文串

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size < 2:
            return s
        max_len =1
        res=s[0]

        for i in range(size):
            p1,len1 = self.help(s,size,i,i)
            p2,len2 = self.help(s,size,i,i+1)

            cur_max = p1 if len1 >= len2 else p2

            if len(cur_max) > max_len:
                max_len = len(cur_max)
                res = cur_max

        return res

    def help(self,s,size,left,right):
        i = left
        j = right

        while i >=0 and j < size and s[i]==s[j]:
            i -=1
            j +=1
        return s[i+1:j],j-i-1