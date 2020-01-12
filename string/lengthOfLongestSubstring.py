# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/5 

'''
3. 无重复字符的最长子串

给定一个字符串，返回它最长的无重复的子串的长度
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

思路：
双指针 i，j 均为 0
如果 s[j] 不在s[i:j] j+=1
否则 i +=1
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        最优解
        如果右侧在hash表中，则更新left为 right 值所在位置+1
        :param s:
        :return:
        '''
        left,right=0,0
        res=0
        pos_dic={}
        for right in range(len(s)):
            if s[right] in pos_dic:
                left=max(left,pos_dic[s[right]]+1)
            pos_dic[s[right]]=right
            res=max(res,right-left+1)
        return res

    def length(self,s):
        i , j =0 ,0
        res = 0
        while i < len(s):
            if j < len(s) and s[j] not in s[i:j]:
                j += 1
            else:
                i += 1
            res = max(res,j-i)
        return res

    def lllll(self,s):
        '''
        时间复杂度O(n)
        :param s:
        :return:
        '''
        lookup=list()
        max_len,cur_len=0,0
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup.append(s[i])
                cur_len +=1
            else:
                index = lookup.index(s[i])
                lookup = lookup[index+1:]
                lookup.append(s[i])
                cur_len = len(lookup)
            max_len = max(max_len,cur_len)
        return max_len


if __name__=='__main__':
    s=Solution()
    a = s.lengthOfLongestSubstring("abccdxccfagcefghji")
    print(a)
    print(s.length("abcabcbb"))
