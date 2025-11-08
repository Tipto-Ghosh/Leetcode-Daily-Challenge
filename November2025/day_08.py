class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        k = 0
        mask = 1
        
        while mask <= n:
            if n & mask:
                ans = 2 ** (k + 1) -1 - ans 
            
            k += 1
            mask <<= 1
        
        return ans 

sol = Solution()
print(sol.minimumOneBitOperations(3))