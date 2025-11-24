from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """ 
        Every time we append a bit(0/1) then current number get's double.
        so always current decimal value will be curr = prev_num * 2 + curr_bit
        Always check it is divisible by 5 or not. 
        
        Time Complexity: O(n) cause we are traversing the array once
        Space Complexity: O(n) cause we are n length array to store the answer.
        """
        
        ans = [] # store the ans
        curr = 0 # current decimal value
        
        for bit in nums:
            # find the current number using: curr*2 + b cause curr is now prev number for this iteration
            curr = curr * 2 + bit 
            # mod it by 5
            curr %= 5
            # if remainder is 0 then True else False
            ans.append(curr == 0)
         
        return ans 
    
sol = Solution()
print(sol.prefixesDivBy5([0,1,1]))
print(sol.prefixesDivBy5([1,1,1]))
print(sol.prefixesDivBy5([1,1,0,0,0,1,0,0,1]))