# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/5 

'''
给定一个字符串，返回它最长的无重复的子串的长度
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left,right=0,0
        res=0
        pos_dic={}
        for right in range(len(s)):
            if s[right] in pos_dic:
                left=max(left,pos_dic[s[right]]+1)
            pos_dic[s[right]]=right
            res=max(res,right-left+1)
        return res
if __name__=='__main__':
    s=Solution()
    a = s.lengthOfLongestSubstring("abcdxcfagc")
    print(a)
