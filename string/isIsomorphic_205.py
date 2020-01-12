# coding=utf-8
# Time: 2019-12-20-11:09 
# Author: dongshichao

'''
205.同构字符串

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true


'''

from collections import Counter
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return list(map(s.index,s))==list(map(t.index,t))


    def isIII(self, s, t):
        '''
        要想同构，那么s 和 t 中的字母，必须是 一一 对应的关系
        一对多 a-b , a-c 不行
        多对一 b-a , c-a 不行
        hash用来保存 对应关系
        aabc  eefg
        a-e
        b-f
        c-g
        :param s:
        :param t:
        :return:
        '''
        hash = {}
        for i ,c in enumerate(s):
            if hash.get(c):
                if hash[c] != t[i]:
                    return False
            else:
                if t[i] in hash.values():
                    return False
                hash[c] = t[i]
        return True


s=Solution()
print(s.isIsomorphic("abba","abab"))

ss="abab"
print(list(map(ss.index,ss)))