# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/23

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
输入: [4,1,2,1,2]
输出: 4
'''

class solution():
    def singleNumber(self,nums):
        '''
        任何数与自己异或为0
        任何数与0异或都是自己
        :param nums:
        :return:
        '''
        num = 0
        for i in nums:
            num = num ^ i
        return num

        # s={}
        # for i in nums:
        #     if i in s.keys():
        #         s.pop(i)
        #     else:
        #         s[i]=1
        # print(list(s.keys())[0])

if __name__=='__main__':
    s=solution()
    nums = [0,0,1,1,2,2,3,3,4]
    a=s.singleNumber(nums)
    print(a)
    print(1^2^1)