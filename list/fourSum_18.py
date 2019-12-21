# coding=utf-8
# Time: 2019-12-20-14:31 
# Author: dongshichao


'''
18.四数字和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

思路：
思路同 三数之和
固定两个数 l , r
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        if sum(nums[:4]) > target:
            return []

        res= []
        print(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):

                l = j+1
                r = n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target and [nums[i],nums[j],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l]==nums[l+1]:
                            l+=1
                        while l < r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif s > target:
                        r -=1
                    else:
                        l +=1

        return res

s=Solution()
print(s.fourSum([0,1,5,0,1,5,5,-4],11))


