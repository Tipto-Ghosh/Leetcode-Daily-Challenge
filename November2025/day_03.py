from typing import List 

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0 # total time needed
        n = len(colors)
        
        for i in range(1 , n):
            # if consicutive
            if colors[i - 1] == colors[i]:
                total_time += min(neededTime[i] , neededTime[i - 1])
                neededTime[i] = max(neededTime[i] , neededTime[i - 1])
        
        return total_time
    
sol = Solution()
print(sol.minCost("abaac" , [1,2,3,4,5]))