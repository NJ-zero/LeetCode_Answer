# coding=utf-8
# Time: 2019-11-21-17:37 
# Author: dongshichao

'''
139. 单词拆分

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)

        dp = [False for _ in range(n)]
        # dp[i]表示 以s[i] 结尾的子字符串是否可以拆分一个活多个在字典中出现的单词

        dp[0]  = s[0] in wordDict

        for r in range(1,n):
            if s[:r+1] in wordDict:
                dp[r] = True
                continue

            for l in range(r):
                if dp[l] and s[l+1:r+1] in wordDict:
                    dp[r] = True
                    break

        return dp[-1]

