# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/9/12 

'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
案例:
s = "leetcode"
返回 0.
s = "loveleetcode",
返回 2.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count={}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] +=1
            else:
                count[s[i]]=1

        print(count)

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        else:
            return -1


if __name__=='__main__':
    s=Solution()
    ss="loveleetcode"
    i = s.firstUniqChar(ss)
    print(i)