from typing import List 
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count_1 = 0 # count number of 1's
        g = 0 # gcd of all elements
        
        for x in nums:
            if x == 1:
                count_1 += 1
            g = math.gcd(g , x)
        
        if count_1 > 0:
            return n - count_1
        
        if g > 1:
            return -1
        
        min_len = n 
        for i in range(n):
            g = 0
            for j in range(i , n):
                g = math.gcd(g , nums[j])
                if g == 1:
                    min_len = min(min_len , j - i + 1)
                    break
        
        return min_len + n - 2
        
        
sol = Solution()
print(sol.minOperations(nums = [2,6,3,4]))
print(sol.minOperations([2,10,6,14]))         