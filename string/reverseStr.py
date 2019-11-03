# coding=utf-8
# Time: 2019-10-19-11:11 
# Author: dongshichao

'''
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。
如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"

思路：
res=""来记录结果
每2K范围，翻转前K个，k:2k 不变


第二种比较进阶

'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <=1 or k == 1 :
            return s
        res=""
        n= len(s)//(2*k)
        for i in range(1,n+1):
            res += s[(i-1)*2*k:i*2*k-k][::-1]
            res += s[(i-1)*2*k+k:i*2*k]

        m = len(s)-n*2*k
        if m == 0:
            return res
        if m < k:
            res += s[len(s)-m:][::-1]
        else:
            res += s[len(s)-m:len(s)-m+k][::-1] +s[len(s)-m+k:]
        return res

    def revvv(self,s,k):
        if len(s) <= k :
            return s[::-1]
        elif len(s) >k and len(s) < 2*k:
            return s[0:k][::-1]+s[k:]
        else:
            return s[0:k][::-1]+s[k:2*k] + self.revvv(s[2*k:],k)

s= Solution()
print(s.reverseStr("abcdefghihrg",2))
print(s.revvv("abcdefghihrg",2))

