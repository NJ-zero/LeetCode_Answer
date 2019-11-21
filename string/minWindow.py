# coding=utf-8
# Time: 2019-11-05-19:05 
# Author: dongshichao
'''
76. 最小覆盖子串

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i, j = 0, 0
        dic_t={}
        for n in t:
            if n in dic_t:
                dic_t[n] += 1
            else:
                dic_t[n] = 1
        _need = sum(dic_t.values()) > 0   #是否需要扩展
        while j < len(s) or not _need:
            if _need:
                if s[j] in dic_t:
                    dic_t[s[i]] -=1     #包含一个就删去一个 词频
                    _need = any(map(lambda x : x>0, dic_t.values()))   #有一个value大于0 就是True,说明没有全部包含
                j +=1
            else:                     #已经全部包含，所有的value都 小于等于 0
                if j < len(s):
                    res=s[i:j]
                if s[i] in dic_t:
                    dic_t[s[i]] += 1
                    _need = any(map(lambda x : x>0, dic_t.values()))
                i += 1

        if len(res) > len(s):
            return ""
        return res


dic={1:2,3:1,4:2,6:-1}
print(sum(dic.values()))
print(any(map(lambda x : x>0, dic.values())))
dic={}
t="abcac"
for i in t:
    dic[i] = dic.get(i, 0) + 1

print(dic)


