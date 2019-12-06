# coding=utf-8
# Time: 2019-08-20-20:17 
# Author: dongshichao

'''
567.字符串的排列

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


思路：
定一个长度和s1 相等的 滑窗，如果滑窗内各元素统计的值相等，则true
不等，则右滑，减去最左边元素，最右边新进来的加一
'''

from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        i, j = 0, n-1
        c = Counter(s1)
        s = Counter(s2[i:j])
        if n > m:
            return False

        while j < m:
            s[s2[j]] +=1
            if c==s:
                return True
            # 每次切片都counter耗时过长，每次窗口增加最右边元素，减少最左边元素
            # 如果最左边的元素已经是0了，则删除这个元素
            s[s2[i]] -= 1
            if s[s2[i]] == 0:
                del s[s2[i]]
            i +=1
            j +=1
        return False

if __name__=='__main__':
    s=Solution()
    a = s.checkInclusion("a","ab")
    print(a)




