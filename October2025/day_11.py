from typing import List 
from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """ 
        For any spell(index) we have 2 option: Take the spell or skip the spell.
        We can only take the spell if we are allowed to take based on 4 given conditions.
        
        since the problem only depends on the damage values and their sums, 
        we can reduce it to a dynamic programming problem similar to “House Robber” — but with a distance constraint of 2 on both sides 
        (i.e., you can't pick neighbors within ±2).
        """
        
        count = Counter(power)
        # total damage contibuted by each unique spell
        total_damage = {p : p * c for p , c in count.items()}
        
        # sort the unique spells
        unique = sorted(total_damage.keys())
        n = len(unique)
        
        dp = [0] * n # dp[i] = max damage till i-th spell
        dp[0] = total_damage[unique[0]]
        
        # now calculate from 1 to n-1 cause 0-th index is already done.
        for i in range(1 , n): 
            # option-1: Skip current index: so ans would be previous one
            not_take = dp[i - 1]
            
            # option-2: Take current index: find last non-conflicting index
            idx = bisect.bisect_right(unique , unique[i] - 3) - 1
            take = total_damage[unique[i]]
            
            if idx >= 0:
                take += dp[idx]
            
            dp[i] = max(take , not_take)
        
        return dp[-1]
        
sol = Solution()
print(sol.maximumTotalDamage([1,1,3,4]))
print(sol.maximumTotalDamage([7,1,6,6]))  
      