# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/27 
'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，
并且 i 和 j 的差的绝对值最大为 k。

输入: nums = [1,2,3,1], k = 3
输出: true
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        dic_num={}
        for i in range(length):
            if nums[i] not in dic_num:
                dic_num[nums[i]]=i
            else:
                if i - dic_num[nums[i]] <=k:
                    return True
                else:
                    dic_num[nums[i]] = i
        return False


if __name__ == "__main__":
    s= Solution()
    print(s.containsNearbyDuplicate([1,2,3,1],5))
