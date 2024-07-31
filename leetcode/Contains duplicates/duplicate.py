class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        # set() is used to keep track of elements 
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
                #used to add element for future lookups
        return False
  
  