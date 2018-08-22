# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class solution():
    def twosum(self,nums,target):
        length = len(nums)
        print(length)
        i = 0
        while i < length:
            other = target - nums[i]
            for j in range(i + 1, length):
                if other == nums[j]:
                    return (i, j)
            i += 1
if __name__=='__main__':
    s=solution()
    a,b=s.twosum([3,5,4,8],7)
    print(a,b)
