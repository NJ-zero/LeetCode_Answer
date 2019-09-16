# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/6 

'''
反转该字符串中的元音字母
'''

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

    def vers(self,s):
        ss = list(s)
        n = len(s)
        i ,j = 0, n-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i<j :
            if ss[j] not in vowels:
                j -= 1
                continue
            if ss[i] not in vowels:
                i += 1
                continue

            ss[i],ss[j] = ss[j],ss[i]
            i += 1
            j -= 1

        return "".join(ss)


if __name__=="__main__":
    s=Solution()
    ss=s.reverseVowels("leetcode")
    print(ss)
    a="aassddccx"
    print(a[::-1])

    print(s.vers("leetcode"))