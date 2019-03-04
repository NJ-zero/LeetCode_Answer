# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/4 

'''
check ip能否ping通
'''

import subprocess
import os

def ping(ip):
    for i in ip:
        # res=subprocess.Popen("ping %s"%i,shell=True,stdout=subprocess.PIPE).stdout.read()
        res=os.system("ping %s"%i)
        print(res)


ping(['123.56.207.119'])