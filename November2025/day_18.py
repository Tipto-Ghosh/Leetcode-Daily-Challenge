from typing import List 

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            i += bits[i] + 1
        
        return i == n - 1

sol = Solution()
print(sol.isOneBitCharacter([1,0,0]))
print(sol.isOneBitCharacter([1,1,1,0]))