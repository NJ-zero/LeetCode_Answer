# coding=utf-8
# Time: 2020-01-15-13:48 
# Author: dongshichao

'''
16进制加法
'''


base=[str(x) for x in range(10)] + [chr(x) for x in range(ord("A"),ord("A")+6)]
print(base)
def tentrans(num):
    res=[]
    while True:
        num,mod = divmod(num,16)
        res.append(base[mod])
        if num == 0:
            break
    print(res)
    res_num = ''.join(res[::-1])
    return res_num


print(tentrans(160))

def sixteentoten(num):
    str_num = num[::-1]
    res=0
    for i in range(len(str_num)):
        res += 16 ** i * base.index(str_num[i])
    return res

print(sixteentoten('A8'))

def sixteenadd(num1,num2):
    num1_str = str(num1)[::-1]
    num2_str = str(num2)[::-1]
    flag = 0
    m,n = len(num1_str),len(num2_str)
    i=0
    res=[]
    while True:
        sum = 0
        if i < m:
            sum += base.index(num1_str[i])
        if i < n:
            sum += base.index(num2_str[i])
        sum += flag
        flag = sum //16
        sum = base[sum % 16]
        res.append(sum)
        i+=1
        if i >= m and i >= n:
            break

    if flag==1:
        res.append("1")
    if res[0] == '0':
        res=res[1:]
    print(res)
    print(''.join(str(x) for x in res[::-1]))

sixteenadd('F','1')


