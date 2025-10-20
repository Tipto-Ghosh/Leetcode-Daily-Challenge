from typing import List 

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0 # initially X = 0
        
        for op in operations:
            # if ++X or X++
            if op[0] == '+' or op[-1] == '+':
                val += 1
            else:
                val -= 1
        
        return val 
    
sol = Solution()

print(sol.finalValueAfterOperations(["++X","++X","X++"]))