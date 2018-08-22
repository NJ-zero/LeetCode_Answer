# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 
'''
翻转整数 123、321   -123 、-321   120 、21
数值范围是 [−2**31,  2**31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0
:param x:
:return:
'''

class solution():
    def reverseint(self,x):
        if x <= -(2 ** 31) or x >= 2 ** 31 or x == 0:
            return 0
        else:
            num = str(x)
            if num[0] == '-':
                num = "-" + num[::-1][:-1]
                i = 0
                while i < len(num):
                    if num[1] == 0:
                        num = num[0] + num[2:]
                    else:
                        break
                    i += 1
                if int(num) <= -(2 ** 31):
                    return 0
                else:
                    return int(num)
            else:
                num = num[::-1]
                i = 0
                while i < len(num):
                    if num[0] == '0':
                        num = num[1:]
                    else:
                        break
                    i += 1
                if int(num) >= 2 ** 31:
                    return 0
                else:
                    return int(num)
if __name__=='__main__':
    s=solution()
    a = s.reverseint(1534236469)
    print(a)
