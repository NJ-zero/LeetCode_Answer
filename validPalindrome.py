# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/7 


'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        else:
            n=len(s)
            left=0
            right=n-1
            while left<right:
                if s[left]!=s[right]:
                    return self.cmp(s,left+1,right) or self.cmp(s,left,right-1)
                left+=1
                right-=1
            return True

    def cmp(self,s,left,right):
        while left<right:
            if s[left] != s[right]:
                return False

            left+=1
            right-=1
        return True

if __name__=="__main__":
    s=Solution()
    print(s.validPalindrome("tebbem"))