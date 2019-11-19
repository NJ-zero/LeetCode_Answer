# coding=utf-8
# Time: 2019-11-19-16:56 
# Author: dongshichao

'''
424. 替换后的最长重复字符
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 10^4。

输入:
s = "ABAB", k = 2
输出:
4
解释:
用两个'A'替换为两个'B',反之亦然。
示例 2:

输入:
s = "AABABBA", k = 1
输出:
4
解释:
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

思路：
维护当前窗口 最大字符词频 ，如果 j-i+1 - maxfreq >k 这时，怎么替换都不会成功
所以窗口 i 往前移一个
'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        i,j=0,0
        maxfreq,res=0,0

        while j < len(s):
            count[s[j]] = count.get(s[j],0)+1
            maxfreq = max(maxfreq,count[s[j]])
            if j-i+1 - maxfreq > k:
                count[s[i]] -=1
                i +=1
            j+=1
            res = max(res,j-i)

        return res

s=Solution()
print(s.characterReplacement(s = "AABABBA", k = 1))