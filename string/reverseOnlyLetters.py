# coding=utf-8
# Time: 2019-10-17-14:26 
# Author: dongshichao

'''
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

双指针

'''

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S=list(S)
        if len(S) <=1:
            return S
        i,j = 0,len(S)-1
        while i < j :
            if not S[i].isalpha():
                i += 1
                continue
            if not S[j].isalpha():
                j -= 1
                continue
            S[i],S[j] = S[j],S[i]
            i+=1
            j-=1
            print(S)
        return "".join(S)

s=Solution()
print(s.reverseOnlyLetters("7_28}"))