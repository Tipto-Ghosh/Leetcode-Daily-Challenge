from typing import List 
from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """ 
        Task: Find the maximum MEX(the smallest number starting from 0 that doesn't appear in the array.)
        
        Find all the MOD value of nums
        Then start from 0 and to till we can make MEX.
        Always ask can we make MEX 0? if no then ans is 0, if yes then ask can we make MEX = 1?
        Go untill the answer is not NO. If No then return the value
        """
        n = len(nums)
        
        track_mod_freq = defaultdict(int)
        
        for i in range(n):
            mod = nums[i] % value
            track_mod_freq[mod] += 1
        
        # now start finding MEX from 0
        mex = 0
        while True:
            residue = mex % value
            # if we have at least one number that can form this residue
            if track_mod_freq[residue] > 0:
                track_mod_freq[residue] -= 1 # use it
                # update mex to next number
                mex += 1
            else:
                # we can't form residue 
                return mex 
        
sol = Solution()

print(sol.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5))
print(sol.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7))
print(sol.findSmallestInteger(nums = [3,0,3,2,4,2,1,1,0,4], value = 5))