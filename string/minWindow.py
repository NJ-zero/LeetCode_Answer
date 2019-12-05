# coding=utf-8
# Time: 2019-11-05-19:05 
# Author: dongshichao
'''
76. 最小覆盖子串

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

思路二：
1. 初始，left指针和right指针都指向S的第一个元素.
2. 将 right 指针右移，扩张窗口，直到得到一个可行窗口，亦即包含T的全部字母的窗口。
3. 得到可行的窗口后，将left指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。
4. 若窗口不再可行，则跳转至 2。



'''
from collections import Counter

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

    def mmmm(self,s,t):

        dic_t={}
        for i in t:
            dic_t[i] = dic_t.get(i,0)+1
        i,j=0,0
        window_t=Counter() # 统计滑窗中每个字出现的次数
        res=""
        min_len=len(s)
        while j < len(s):
            n = s[j]
            window_t[n] +=1
            j +=1

            while all(map(lambda x: window_t[x] >= dic_t[x], dic_t.keys())): #说明滑窗已包含全部t的元素
                if j-i <= min_len:
                    res = s[i:j]
                    min_len = j-i
                window_t[s[i]] -= 1 # 起点往左移
                i += 1
        return res



s=Solution()
print(s.mmmm("ADOBECODEBANC","ABC"))

dic={1:2,3:1,4:2,6:-1}
print(sum(dic.values()))
print(any(map(lambda x : x>0, dic.values())))



