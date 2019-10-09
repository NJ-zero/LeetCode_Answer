# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/6 

'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

解题思路：
1.确定元素是不是 字母 用 isalnum() 函数
2.双指针，一个从前往后，一个从后往前
'''

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=re.sub('[^a-z0-9]','',s.lower())
        print(s)
        return s==s[::-1]
    def is_s(self,s):
        s= ''.join(filter(str.isalnum(),s)).lower()
        return s==s[::-1]

    def is_dd(self,s):
        n= len(s)
        i,j = 0,n-1
        while i < j:
            if s[i].isalnum() == False:
                i+=1
                continue
            if s[j].isalnum() == False:
                j -=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

if __name__=='__main__':
    s=Solution()
    a=s.isPalindrome("A man, a plan, a canal: Panama")
    print(a)

    a = s.is_dd("A man, a plan, a canal: Panama")
    print(a)