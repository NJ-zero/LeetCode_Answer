# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/30 

'''
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。

当 needle 是空字符串时我们应当返回 0
注意两个都为空的情况
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if  haystack != "":
            return haystack.find(needle)
        else :
            if needle=="":
                return 0
            else:
                return -1
    def strStr2(self, haystack, needle):

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] ==needle:
                return i
        return -1


if __name__ == "__main__":
    s =Solution()
    print(s.strStr2("","a"))
