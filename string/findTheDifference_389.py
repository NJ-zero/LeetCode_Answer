# coding=utf-8
# Time: 2019-12-17-15:36 
# Author: dongshichao

'''
389.找不同
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

 
示例:
输入：
s = "abcd"
t = "abcde"
输出：
e

解释：
'e' 是那个被添加的字母。


'''

from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_s = Counter(s)
        for i in t:
            if i in dic_s and dic_s[i] > 0:
                dic_s[i] -=1
            elif i not in dic_s or dic_s[i] == 0:
                return i