# coding=utf-8
# Time: 2019-10-15-16:36 
# Author: dongshichao

'''
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。

至少有一个空座位，且至少有一人坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。

示例 1：

输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。
示例 2：

输入：[1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。

1.对于两端的连续0，最大距离等于连续0的个数，对于中间的最大距离等于连续0的个数加1在除以2


'''

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        i = start = count = 0

        # 先從開頭算
        while seats[i] == 0: i += 1
        count = i
        # 再從結尾算
        j = len(seats) - 1
        while seats[j] == 0: j -= 1

        count1 = len(seats) - 1 - j
        if count1 > count:
            count = count1

        #start表示当前计数
        while i < len(seats):
            if seats[i]==0:
                start +=1
            else:
                if (start+1) //2 > count:
                    count = (start +1 )//2
                start = 0
            i +=1
        return count

    def ssss(self,seats):
        persons = [p for p, seat in enumerate(seats) if seat == 1]
        print(persons)
        return max(persons[0], len(seats) - 1 - persons[-1], max([(persons[r] - persons[r - 1]) // 2 for r in range(1, len(persons))]+[0]))


s= Solution()
print(s.maxDistToClosest([1,0,0,0,0,0,0,]))
print(s.ssss([1,0,0,0,0,0,0,1]))
