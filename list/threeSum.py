# coding=utf-8
# Time: 2019-11-06-16:12 
# Author: dongshichao

'''
15.三数之和

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


思路：
先排序
长度 小于 3 返回 【】
三个指针， L=i+1 i R=n
i遍历整个数组
nums[i] <= nums[L] <= nums[R]
所以nums[i] > 0 就跳出



当 nums[i]+nums[L]+nums[R] == 0 时：执行循环
判断左界 和 右届 是否和下一位置重复，则跳过，L+1  /  R-1
当三数之和 大于 0，说明 nums[R] 太大，R左移
当三数之和 小于 0，说明 nums[L] 太小，L右移


'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <3:
            return []
        nums.sort()
        if nums[0] >1 or nums[-1] <0:
            return []

        n=len(nums)
        res=[]
        for i in range(n):
            if nums[i] > 0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            L = i+1
            R = n-1
            while L<R:
                if nums[i]+nums[L]+nums[R] == 0:
                    res.append([nums[i],nums[L],nums[R]])
                    while (L<R and nums[L]==nums[L+1]):
                        L += 1
                    while (L<R and nums[R]==nums[R-1]):
                        R -= 1
                    L+=1
                    R-=1
                elif nums[i]+nums[L]+nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return res


s=Solution()
print(s.threeSum([0,0,0]))
