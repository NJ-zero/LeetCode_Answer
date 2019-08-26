# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/4/11 

'''
将数组组合成最大的数
[12,23,544,68,9]
9685442312
'''

def MaxNumbers(numbers):
    s_numbers = [str(i) for i in numbers ]
    len_s = len(s_numbers)
    for i in range(len_s):
        for j in range(i+1,len_s):
            if s_numbers[i]+s_numbers[j]<s_numbers[j]+s_numbers[i]:
                s_numbers[i],s_numbers[j]=s_numbers[j],s_numbers[i]

    print(''.join(s_numbers).lstrip())


s=[12,23,544,68,9]
MaxNumbers(s)

'''
输入: [1,8,6,2,5,4,8,3,7]
输出: 49

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
'''

def maxArea(s):
    n = len(s)
    i ,j = 0 ,n-1
    area = 0
    while i < j:
        area = max(area,min(s[i],s[j]) * (j-i))
        if s[i] < s[j]:
            i+=1
        else:
            j-=1
    return area

s= [1,8,6,2,5,4,8,3,7]
print(maxArea(s))