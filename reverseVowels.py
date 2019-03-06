# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/6 



class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=['a','e','i','o','u','A','E','I','O','U']
        vo_s=[]
        for i in s:
            if i in vowels:
                vo_s.append(i)
        s_list=list(s)
        s_len=len(s_list)
        for i in range(s_len):
            if s[i] in vowels:
                s_list[i] = vo_s.pop()
        return ''.join(s_list)

if __name__=="__main__":
    s=Solution()
    ss=s.reverseVowels("leetcode")
    print(ss)
    a="aassddccx"
    print(a[::-1])