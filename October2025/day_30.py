from typing import List 

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """ 
        In operation we are raising one sub-array one step ahead.
        If we have a increasing order then we need to apply operations. Otherwise no operations needed.
        """
        n = len(target)
        operations = 0
        prev = 0
        
        for i in range(n):
            curr = target[i]
            
            if curr > prev:
                operations += (curr - prev)
            
            prev = curr
            
        return operations
    
sol = Solution()
print(sol.minNumberOperations([3,1,5,4,2]))