# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
判断是否是回文数
121   1221
'''

class solution():
    def isPalindrome(self,x):
        # x=str(x)
        # return x == x[::-1]

        pre=x
        back=0
        while pre >0:
            back = back*10 + pre %10
            pre = pre // 10
        return back == x

if __name__=='__main__':
    s=solution()
    a=s.isPalindrome(124421)
    print(a)