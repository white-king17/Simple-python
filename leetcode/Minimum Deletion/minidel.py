class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count=0
        minidel=0
        for char in s:             #iterates through all charcters in s
            if(char=="a"):
                minidel=min(minidel+1,b_count)
                #We take minimum of two
                #minidel+1 for deleting the current 'a' or b_count for converting all previous 'b' to 'a'
            else:
                b_count += 1
        return minidel