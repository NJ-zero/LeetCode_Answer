# coding=utf-8
# Time: 2019-10-19-14:56 
# Author: dongshichao

'''
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

示例 2：
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"

示例 3：
输入：str1 = "LEET", str2 = "CODE"
输出：


'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        解题失败
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = len(str1)
        m = len(str2)
        if m > n:
            s = str1
        else:
            s = str2
        res=""
        for i in range(1,len(s)//2+1):
            if(len(s)%i==0):
                if s[0:i]*(len(s)//i)==s:
                    res=s[0:i]
                    break
        print(res)
        if len(res)!=0 and res*(n//len(res)) == str1 and res*(m//len(res)) ==str2:
            return res
        else:
            if n >=m :
                if str1 == str2 * (n // m):return str2
            elif m >n :
                if str2 == str1 * (n // m):return str1

        return res

    def gcd(self,str1,str2):
        if len(str1) < len(str2):
            str1, str2 = str2, str1  # 将短的字符串赋给str2
        len_str1 = m = len(str1)
        len_str2 = n = len(str2)
        res = ''
        while n > 0:
            m, n = n, m % n  # 辗转相除法求最大公因子
        gcd = m
        rep1, rep2 = str1[:gcd], str2[:gcd]
        # 判断最大公因子对应的前缀是否相等，以及是否能构成字符串str1和str2
        if rep1 == rep2 and str1 == len_str1 // gcd * rep1 and str2 == len_str2 // gcd * rep2:
            return rep1
        return res


s=Solution()
print(s.gcdOfStrings("NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM","NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"))




