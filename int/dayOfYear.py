# coding=utf-8
# Time: 2019-11-08-11:34 
# Author: dongshichao
'''
1154.一年中的第几天

给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。


示例 1：

输入：date = "2019-01-09"
输出：9
示例 2：

输入：date = "2003-03-01"
输出：60

提示：
date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字。
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。

思路：
判断一下闰年：能被4整除且不能被100整除


'''

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year,month,day=int(date.split('-')[0]),int(date.split('-')[1]),int(date.split('-')[2])
        _isrunnian=False
        if year % 4 ==0 and year %100!=0:
            _isrunnian=True

        month30_count=[4,6,9,11]
        month31_count=[1,3,5,7,8,10,12]

        count=0
        if month>2 and _isrunnian:
            count += 29
        elif month >2 and not _isrunnian:
            count += 28
        for i in range(month):
            if i in month30_count:
                count += 30
            elif i in month31_count:
                count += 31

        count += day
        return count

s=Solution()
print(s.dayOfYear("1900-03-25"))


