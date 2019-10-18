# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/24

'''
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：
全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

三种场景：
1。首字母大写
2。全部大写
3。全部小写
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word or word.lower() == word or word.capitalize() == word:
            return True
        else:
            return False

if __name__=="__main__":
    s=Solution()
    word = "FlaG"
    a=s.detectCapitalUse(word)
    print(a)
    s="addd"
    print(s.capitalize())