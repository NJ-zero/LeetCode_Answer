# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
9. 回文数
判断是否是回文数
121   1221

思路：
1.整除法

2。转换为string
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

    def isPanlidromestr(self,x):
        '''
        转化为str
        :param x:
        :return:
        '''
        x = str(x)
        return  x == x[::-1]

    def issss(self,x):
        x = str(x)
        i,j=0,len(x)-1
        while i <j :
            if x[i] != x[j]:
                return False
            i+=1
            j-=1

        return True

if __name__=='__main__':
    s=solution()
    a=s.isPalindrome(124421)
    print(a)
    print(s.issss(11331))