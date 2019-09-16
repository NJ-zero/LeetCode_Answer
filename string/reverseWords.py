# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/10/8

'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl=s.split(" ")
        for i in range(len(sl)):
            sl[i]=(sl[i][::-1])
        print(sl)
        sl = [ i for i in sl if i != ""]
        return (" ".join(sl))


if __name__=='__main__':
    s=Solution()
    a = s.reverseWords("a  ab  c     cdd")
    print(a)