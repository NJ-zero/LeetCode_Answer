# coding=utf-8
# Time: 2019-12-07-16:54 
# Author: dongshichao
'''
12. 整数转罗马数字


'''



class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dic={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }

        res=""
        for key in sorted(roman_dic.keys())[::-1]:
            s = num //key
            if s == 0:
                continue
            res += s * roman_dic[key]
            num -= s * key
            if num == 0:
                break
        return res

s = Solution()
print(s.intToRoman(4996))