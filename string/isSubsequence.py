# coding=utf-8
# Time: 2019-10-30-17:17 
# Author: dongshichao
'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.


'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_S= len(s)
        l_t= len(t)
        i,j = 0,0
        while i < l_S and j < l_t:
            if s[i] == t[j]:
                i+=1
            j+=1

        return i==l_S

    def isSubbbb(self,s, t):
        if not s:
            return True
        for i in s:
            res= t.find(i)
            if res == -1:
                return False
            else:
                t= t[res+1:]
        return True

s=Solution()
print(s.isSubsequence("abdc","aggggggbjc"))