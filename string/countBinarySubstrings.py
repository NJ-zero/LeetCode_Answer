# coding=utf-8
# Time: 2019-10-21-16:08 
# Author: dongshichao

'''
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

思路：
使用一个长度为2的滑窗，遍历整个字符串，遇到 滑窗内两个数字不一样，则左右扩张

'''



class Solution(object):
    def countBinarySubstrings(self, s):
        """
        pre用来记录和当前字符不同的字符的个数
        cur用来记录当前字符的个数
        遍历字符串，当第i个字符和第i-1个字符一样时，cur++
        反之，是0和1的交界处，计算pre和cur中更小的值，为有效子串的个数，有多长就有多少个，再将cur赋值给pre作者：wzNote

        :rtype: int
        """
        if len(s) <=1:
            return 0

        pre,cur,res = 0,1,0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur +=1
            else:
                res += min(pre,cur)
                pre,cur = cur,1

        return res + min(pre,cur)

    def countttt(self, s):
        count = 0
        for i in range(len(s)-1):
            left, right=s[i],s[i+1]
            l,r=i,i+1
            if left != right:
                while 0<= l < r < len(s) and s[l] == left and s[r] == right:
                    count +=1
                    l -= 1
                    r += 1
        return count

s=Solution()
print(s.countttt("00110011"))