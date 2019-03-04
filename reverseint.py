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
        if -10<x<10:
            return x
        str_x=str(x)
        if str_x[0]!='-':
            str_x=str_x[::-1]
            x=int(str_x)
        else:
            str_x=str_x[1:][::-1]
            str_x='-'+str_x
            x=int(str_x)

        return x if -(2**31)<x<2**31-1 else 0
if __name__=='__main__':
    s=solution()
    a = s.reverseint(-2100)
    print(a)
