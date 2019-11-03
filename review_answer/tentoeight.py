# coding=utf-8
# Time: 2019-10-08-10:01 
# Author: dongshichao

'''
10进制数转8进制数
JD面试题
'''


base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'), ord('A')+6)]

def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        # num, mod = divmod(num, 2)  #### 十进制转为二进制
        # num, mod = divmod(num, 16)   #### 十进制转为十六进制
        num, mod = divmod(num, 8)    #### 十进制转为八进制
        mid.append(base[mod])
    print(mid)
    return ''.join(str(x) for x in mid[::-1])

def tentoeight(num):
    res=[]
    while num != 0 :
        r = num % 8
        num = num // 8
        res.append(r)
    print(res)
    print(''.join(str(x) for x in res[::-1]))

def tentotwo(num):
    res=[]
    while num != 0 :
        r = num % 2
        num = num // 2
        res.append(r)
    print(res)
    print(''.join(str(x) for x in res[::-1]))

def twototen(num):
    str_num=str(num)
    i=0
    sum = 0
    for n in str_num[::-1]:
        sum += int(n) * (2**i)
        i +=1
    print(sum)

print(dec2bin("126"))

tentoeight(17)
tentotwo(18)
twototen(10010)