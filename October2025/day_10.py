from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # n = len(energy)
        # max_eng = - float("INF")
        
        # for i in range(n):
        #     curr = 0
            
        #     j = i 
        #     while j < n:
        #         curr += energy[j]
        #         j += k 
            
        #     max_eng = max(max_eng , curr)
        
        # return max_eng
        
        # optimization
        
        """ 
        If we start at i-th position the total energy we can get is:
            dp[i] = energy[i] + dp[i + k] if i + k < n otherwise
            dp[i] = energy[i] if i + k >= n.
        
        Then final answer will be max(dp[i]) for all position i
        """
        
        n = len(energy)
        dp = [0] * n 
        
        # start from the last index
        for i in range(n - 1 , -1 , -1): 
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        
        return max(dp)

sol = Solution()

print(sol.maximumEnergy(energy = [5,2,-10,-5,1], k = 3))
print(sol.maximumEnergy(energy = [-2,-3,-1], k = 2))