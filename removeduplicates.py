# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

'''
移除列表中重复的元素
如 [0,0,1,1,1,2,2,3,3,4] 返回 [0,1,2,3,4]
'''
class solution():
    def removeduplicate(self,A):
        i=0
        while i < len(A)-1:
            if A[i] == A[i+1]:
                del(A[i])
                continue
            i+=1
        return A


if __name__=='__main__':
    s=solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    a=s.removeduplicate(nums)
    print(a)

