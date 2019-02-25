# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/25

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers == []:
            return 0
        else:
            res = numbers[0]
            count = 0
            for i in range(1, len(numbers)):
                if res == numbers[i]:
                    count += 1
                else:
                    if count == 0:
                        res = numbers[i]
                        count = 1
                    else:
                        count -= 1
            if self.check(res,numbers):
                return res
            else:
                return 0

    def check(self,res, nums):
        if nums.count(res) * 2 > len(nums):
            return True
        else:
            return False

if __name__=='__main__':
    s=Solution()
    ss=[1,2,3,1,1,2,1,1,14,1,5,1,6,1,2,3,1,1]
    i = s.MoreThanHalfNum_Solution(ss)
    print(i)