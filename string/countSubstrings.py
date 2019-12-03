# coding=utf-8
# Time: 2019-11-21-15:31 
# Author: dongshichao

'''
647. 回文子串

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

思路：
方法同 5.最长回文子串
longestPalindrome

'''


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)):
            s1 = self.isppp(s,len(s),i,i)
            s2 = self.isppp(s,len(s),i,i+1)
            sum += s1+s2
        return sum


    def isppp(self,s,size,left,right):
        i = left
        j = right
        count = 0
        while i >=0 and j < size and s[i]==s[j]:
            count +=1
            i -=1
            j +=1

        return count

s=Solution()
print(s.countSubstrings("abcc"))