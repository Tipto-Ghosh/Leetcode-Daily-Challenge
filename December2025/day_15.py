from typing import List 
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        counts = 0
        curr = 1
        
        for day in range(n - 1):
            # if next day's price is 1 less than current day
            if prices[day + 1] == prices[day] - 1:
                curr += 1 
            else:
                counts += (curr * (curr + 1))//2
                curr = 1
        
        counts += (curr * (curr + 1))//2
        
        return counts 

sol = Solution()

print(sol.getDescentPeriods([3,2,1,4]))
print(sol.getDescentPeriods([8,6,7,7]))
print(sol.getDescentPeriods([1]))