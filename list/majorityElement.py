# coding=utf-8
# Time: 2019-09-17-16:23 
# Author: dongshichao

'''
169.多数元素
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

解题思路：
借助额外的空间 一个map

思路二：
遍历nums,把众数+1 其他 -1，全部加起来，结果肯定大于 0
[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
先把 7 记为 众数 ，到 第一个 | 时，计数器变为 0
再把 5 记为 众数 ，到 第二个 | 时，计数器变为 0
忽略了同样多的 众数 和 非众数，剩下的 肯定是 众数

'''



class Solution(object):
    def majorityElement(self, nums):
        """
        时间复杂度 O(n) 空间复杂度 O(n)
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in count:
            if count[i] > len(nums)//2:
                return i


    def mmm(self,nums):
        '''
        时间复杂度 O(n) 空间复杂度 O(1)
        :param nums:
        :return:
        '''
        count = 0
        res = None
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count +=1
            else:
                count -=1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,2,3,4,2,2,2,2,2,2]))
    print(s.mmm([1,2,3,3,3]))