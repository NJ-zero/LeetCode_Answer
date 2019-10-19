# coding=utf-8
# Time: 2019-10-19-14:14 
# Author: dongshichao

'''
我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。

例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，
其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。
提示：

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] 都是小写英文字母

思路：
一个字典用来存

'''

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        queries = [ self.f(i) for i in queries]
        words = [self.f(i) for i in words]
        res=[]
        dic={}
        for i in queries:
            if i in dic:
                res.append(dic[i])
            else:
                sum=0
                for j in words:
                    if i < j:
                        sum+=1
                dic[i] = sum
                res.append(dic[i])
        return res

    def f(self,s):
        '''
        :type s:str
        :rtype: int
        '''
        return s.count(min(s))

s =Solution()
print(s.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))