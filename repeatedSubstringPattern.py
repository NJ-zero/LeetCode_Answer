# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/24

'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

输入: "aba"
输出: False

输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(1,int(length/2) +1):
            if length % i == 0:
                if s==(s[:i] * int(length/i)):
                    return True
                    break
        else:
            return False

if __name__=="__main__":
    s=Solution()
    word = "abcabc"
    a=s.repeatedSubstringPattern(word)
    print(a)