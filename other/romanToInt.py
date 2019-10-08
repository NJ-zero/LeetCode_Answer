# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/5 

'''
罗马数字转整数

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。


'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
                   'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        sp=['IV','IX','XL','XC','CD','CM']
        if s=='IV':
            return 4
        elif s=='IX':
            return 9
        elif s=='XL':
            return 40
        elif s=='XC':
            return 90
        elif s=='CD':
            return 400
        elif s=='CM':
            return 900
        else:
            sum=0
            for ss in sp:
                if ss in s:
                    c=s.count(ss)
                    sum+=c*roman_dic[ss]
                    s=s.replace(ss,'')
                    print(s)
            for i in s:
                if i in roman_dic:
                    sum+=roman_dic[i]
            return sum

    def romamToInttt(self,s):
        roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                     'A': 4, 'B': 9, 'E': 40, 'F': 90, 'G': 400, 'H': 900}
        s=s.replace("IV", "A")
        s=s.replace("IX", "B")
        s=s.replace("XL", "E")
        s=s.replace("XC", "F")
        s=s.replace("CD", "G")
        s=s.replace("CM", "H")
        print(s)
        return sum(roman_dic[i] for i in s)


if __name__=="__main__":
    s=Solution()
    a="XCIV"
    print(s.romanToInt(a))
    print(s.romamToInttt(a))


