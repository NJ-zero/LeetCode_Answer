# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/2/28 

'''
檢查ip地址是否合法
'''

s='1.2.1.1'
print(s.split('.'),len(s))

def check(ip):
    if len(ip)<7 or ip[0]==0:
        return False
    else:
        ips=ip.split('.')
        print(ips)
        for i in ips:
            if int(i) > 255 or int(i)< 0:
                return False
        return True

print(check('1.-2.0.2'))
