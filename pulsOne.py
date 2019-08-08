# coding=utf-8
# Time: 2019-08-08-19:46 
# Author: dongshichao

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits


        # n = 0
        # for i in digits:
        #     n = n*10 + i
        # n +=1
        # strn = str(n)
        # res = []
        # for i in strn:
        #     res.append(i)
        # return res


if __name__=='__main__':
    s=Solution()
    a = s.plusOne([9])
    print(a)
