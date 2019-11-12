# coding=utf-8
# Time: 2019-11-12-19:18 
# Author: dongshichao
'''
93.复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

思路：
ip 需 在 0 - 255 之间，第一段不能为 0
对于有效的判断
0-255 之间，但是 001 这种会有问题，所以 要加 str(int(num))==num

w1+,+w2+,+w3+,+w4构成
w1 i必须在 1在3位 【1：4】 w1=[:i]
w2 j 必须在【i+1，i+4】   w2=[i:j]
w3 k 必须在【j+1，j+4】   w3=[j:k]
w4=[k:]

'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isNUm(num):
            if num and 0 <=int(num)<=255 and str(int(num))==num:
                return True
            return False
        res=[]
        for i in range(1,4):
            w1=s[:i]
            if not isNUm(w1):
                continue

            for j in range(i+1,i+4):
                w2=s[i:j]
                if not isNUm(w2):
                    continue

                for k in range(j+1,j+4):
                    w3,w4=s[j:k],s[k:]
                    if not isNUm(w3) or not isNUm(w4):
                        continue
                    if w1!="0":
                        res.append(w1 + '.' + w2 + '.' + w3 + '.' + w4)
        return res


s=Solution()
print(s.restoreIpAddresses("0000"))