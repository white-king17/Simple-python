class Solution:
    def rangeSum(self, num: List[int], n: int, left: int, right: int) -> int:
        arr=[]      #intialising arr to empty list to store sub array
        for i in range (n):
            s=0
            for j in range (i,n):
                s+=num[j]
                arr.append(s)     # each s appended to array
        arr.sort()         #sorts array in ascending order
        mod=10**9+7        #to prevent overflow , since the result is large
        return sum (arr[left-1:right])%mod