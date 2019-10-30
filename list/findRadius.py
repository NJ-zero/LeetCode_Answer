# coding=utf-8
# Time: 2019-10-30-20:13 
# Author: dongshichao

'''
475.供暖器问题

'''

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.append(float("inf")) # 保证最终index不会越界
        heaters.sort()
        max_dist,index=0,0
        for house in houses:
            while house >= heaters[index]:
                index += 1
            if index >0 :
                curr = min(heaters[index]-house,house-heaters[index-1])
            else:
                curr = abs(heaters[index]-house)
            max_dist = max(max_dist,curr)
        return max_dist