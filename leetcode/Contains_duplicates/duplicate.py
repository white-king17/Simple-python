class Solution:
    def containsDuplicate(self, num: List[int]) -> bool:
        n=len(num)
        for i in range(n-1):
            for j in range(i+1,n):
                if num[i]==num[j]:
                    return True
        return False