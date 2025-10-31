from typing import List 

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num , 0) + 1
            if freq[num] > 1:
                ans.append(num)
        
        return ans 
    
sol = Solution()
print(sol.getSneakyNumbers([0,1,1,0]))