# coding=utf-8
# Time: 2019-09-07-14:28 
# Author: dongshichao

'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true

示例 2:

输入: [1,2,3,4]
输出: false
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <=1:
            return False
        count={}
        for i in nums:
            print(i)
            if i in count:
                print(1)
                return True
            else:
                count[i]=1
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,3]))
