# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/23
'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数
输入: [3,0,1]
输出: 2
输入: [0]  [1]
输出: 1  0
'''
class solution():
    def missingNumber(self,nums):
        # if len(nums)==1:
        #     if nums == [0]:
        #         return 1
        #     if nums == [1]:
        #         return 0
        # else:
        #     if len(nums) > max(nums):
        #         return len(nums)
        #     for i in range(0,sorted(nums)[-1]):
        #         if i not in nums:
        #             return (i)
        num=0
        for i in nums:
            num = i+num
        n=0
        for i in range(max(len(nums)+1,sorted(nums)[-1]+1)):
            n=n+i
        return(n-num)

if __name__=='__main__':
    s=solution()
    nums = [3,0,1]
    a=s.missingNumber(nums)
