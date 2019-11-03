# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class solution():
    def twosum(self,nums,target):
        '''
        暴力解法
        :param nums:
        :param target:
        :return:
        '''
        length = len(nums)
        print(length)
        i = 0
        while i < length:
            other = target - nums[i]
            for j in range(i + 1, length):
                if other == nums[j]:
                    return (i, j)
            i += 1

    def twosum2(self,nums,target):
        '''
            用于数组是有序数组
        :param nums:
        :param target:
        :return:
        '''
        n = len(nums)
        i = 0
        j = n-1
        while i<j:
            sum = nums[i] + nums[j]
            if sum == target:
                return (i,j)
            elif sum < target:
                i+=1
            else:
                j-=1
    def towsum3(self,nums,target):
        '''
        最优解
        :param nums:
        :param target:
        :return:
        '''
        dic ={}
        for i ,num in enumerate(nums):
            a = target - num
            if num in dic:
                return (dic[num],i)
            else:
                dic[a] = i


if __name__=='__main__':
    s=solution()
    a,b=s.twosum([3,5,4,8],7)
    print(a,b)
    a,b=s.twosum2([3,2,4],6)
    print(a,b)