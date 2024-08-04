class Solution:
    def pivotInteger(self, n: int) -> int:
        li,c=[i for i in range(1,n+1)],-1   
              # This is a list comprehension that iterates over each number i in the range i to n+1.
        for i in range(len(li)):
            if sum (li[0:i+1])==sum(li[i:]):    # i+1 is used cover o based index to 1 based index.
            # The if that the sum of the elements from the start to i is equal to the sum of the elements from i to end of list.
                c=i+1
        return c