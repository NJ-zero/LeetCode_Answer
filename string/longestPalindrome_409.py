# coding=utf-8
# Time: 2019-12-17-15:44 
# Author: dongshichao
'''
409. 最长回文串

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

思路：
对于字母，假如他出现了 n 次， 可以让 n //2 * 2个字母 对称 aaaaa ,其中aaaa 是对称的，5 //2 * 2

如果任何一个满足 n % 2 == 1,那么这个数 可以是 中心 bbb ,
针对这种情况， n % 2 ==1 and sum % 2 ==0 ,结果 加 1

'''
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic_s = Counter(s)
        sum = 0
        for i in dic_s:
            sum += dic_s[i] // 2 * 2
            if dic_s[i] % 2 ==1 and sum % 2 == 0:
                sum += 1

        return sum

s=Solution()
print(s.longestPalindrome("aaa"))