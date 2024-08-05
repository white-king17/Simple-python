class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)      # Counetr counts the frequency of the element
        for i in arr:
            if counter[i]==1:       # If i is distinct k is decremented
                k-=1
                if k==0:
                    return i
        return ""