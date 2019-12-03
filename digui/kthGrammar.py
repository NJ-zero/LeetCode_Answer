# coding=utf-8
# Time: 2019-11-04-19:46 
# Author: dongshichao

'''
779.第K个语法符号
在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10
给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）


例子:

输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001

'''
class Solution(object):
    def kthGrammar(self, N, K):
        """
        备注：这个方法会超时
        :type N: int
        :type K: int
        :rtype: int
        """
        res=['0','01','0110']
        dic={0:'01',1:'10'}
        if N <=3 :

            return res[N-1][K-1]
        for i in range(3,N+1):
            s=""
            for j in res[i-1]:
                s += dic[int(j)]
            res.append(s)
        return res[N-1][K-1]
s=Solution()
print(s.kthGrammar(10,120))