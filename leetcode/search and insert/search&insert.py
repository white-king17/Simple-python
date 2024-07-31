class Solution:
    def searchInsert(self, num: List[int], target: int) -> int:
        low,high=0 , len(num)-1
        while(low<=high):
            mid=(low+high)//2
            if num[mid]==target:
                return mid
            if target > num[mid] :
                low=mid+1
            else :
               high=mid-1
        return low