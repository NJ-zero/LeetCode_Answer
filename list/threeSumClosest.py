# coding=utf-8
# Time: 2019-11-18-17:46 
# Author: dongshichao

'''
16. 最接近的三数之和

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

思路：
先排序 后 双指针
固定的ans = 0 + 1 +2
遍历数组，i + i+1 + r
如果三个和大于 target r-1 小于 则 l=i+1 右移 加一
如果 sum==target 返回target
判断 sum和target 之间距离是不是小于 ans和target的距离，更小则，更新ans = sum

'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        n=len(nums)
        ans = nums[0]+nums[1]+nums[2]
        print("ane:",ans)
        for i in range(n):
            l = i+1
            r = len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if abs(target-res) < abs(target-ans):
                    print("res:",res)
                    ans = res
                if res > target:
                    r -=1
                elif res < target:
                    l +=1
                else:
                    return target
        return ans


s= Solution()
print(s.threeSumClosest([1,1,1,0],-100))
