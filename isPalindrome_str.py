# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/6 



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

if __name__=='__main__':
    s=Solution()
    a=s.isPalindrome("A man, a plan, a canal: Panama")