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