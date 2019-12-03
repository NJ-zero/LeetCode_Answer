# coding=utf-8
# Time: 2019-11-06-10:30 
# Author: dongshichao

'''
统计二进制数1的个数
'''

def countone(n):
    c=0
    while n > 0:
        if n & 1 ==1:   # 和1 位与 运算，两个都为 1，结果为 1
            c +=1
            print("c:",c)
        n = n >> 1      # 右移运算符
        print(n)
    return c
print(countone(5))
print(5>>1,5&1)



