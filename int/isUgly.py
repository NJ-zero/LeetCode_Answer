# coding=utf-8
# Time: 2019-11-11-19:45 
# Author: dongshichao

'''
263. 丑数
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。

循环：
能被2 整除 则整除
能被3 整除 则整除
能被5 整除 则整除

一直循环下去，如果等于1 就是 丑数

'''
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 0:
            return False
        while True:
            last = num
            if not num%2:
                num //=2
            if not num % 3 :
                num //= 3
            if not num % 5 :
                num //= 5
            if num ==1 :
                return True
            if last == num :
                return False

    def isss(self, num):
        if num < 0 :
            return False
        for e in [2,3,5]:
            while num % e == 0:
                num = num / e
        return num == 1