# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/9 

'''
最常见的单词
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词
'''

import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ps_list=re.split('[ |,]',paragraph)
        print(ps_list)
        ps_new=[re.sub('[^a-z]','',i.lower()) for i in ps_list if i !='']
        print(ps_new)
        count={}
        for i in ps_new:
            if i not in banned:
                count[i] =1 if i not in count else count[i]+1

        maxlen=max(i for i in count.values())

        for k,v in count.items():
            if v==maxlen:
                return k

if __name__ == '__main__':
    s=Solution()
    print(s.mostCommonWord("a., a, a, a, b,b,b,c, c",["a"]))

