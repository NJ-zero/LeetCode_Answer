# coding=utf-8
# Time: 2019-10-19-14:00 
# Author: dongshichao

'''
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False


思路：
1。统计A出现的次数，大于1 则flase
2. 要求不超过两个连续LL,将LL替换为L,在统计LL出现次数，大于1 则false
'''


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = s.count("A")
        if n >=2 :
            return False
        m = s.replace("LL","L").count("LL")
        if m >=1:
            return False
        return True

a="ALLLPL"
print(a.replace("LL","L"))