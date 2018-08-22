# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/8/22 

class solution():
    def removeduplicate(A):
        # k = 0
        # for i in range(1, len(A)):
        #     if A[i] != A[k]:
        #         k += 1
        #         A[k] = A[i]
        #
        # del A[k + 1:len(A)]
        # return A
        i=0
        while i < len(A)-1:
            if A[i] == A[i+1]:
                del(A[i])
                continue
            print(i,A)
            i+=1
        return A

s=solution
nums = [0,0,1,1,1,2,2,3,3,4]
a=s.removeduplicate(nums)
print(a)

