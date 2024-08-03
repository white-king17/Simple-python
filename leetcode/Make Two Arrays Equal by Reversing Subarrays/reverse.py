class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #counter is the dictionary which counts the frequency of the given list
        return Counter(target)==Counter(arr)