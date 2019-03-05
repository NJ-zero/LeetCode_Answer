# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/5 


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        minl=min([len(x) for x in strs])
        if minl==0:
            return ""
        else:
            for i in range(minl):
                for s in strs:
                    if s[i] == strs[0][i]:
                        pass
                    else:
                        return s[:i]
            return s[:i+1]

if __name__=="__main__":
    s=Solution()
    strs=["a"]
    print(s.longestCommonPrefix(strs))



