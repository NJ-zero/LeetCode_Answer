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