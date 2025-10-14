from typing import List 

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """ 
        Find the first increasing sub-array with k elements.
        Then try to find a new increasing sub-array from the next index.
        
        So basically we have to find 2 increasing sub-array first one nums[a....a + k]
        second one nums[b....b + k] where b = a + k
        so in short we have to find a single increasing sub-array with length 2k.
        """
        n = len(nums)
        
        def is_increasing(start: int) -> bool:
            """check if nums[start : start + k] is strictly increasing or not"""
            
            # if not enough elements
            if start + k > n:
                return False
            
            for i in range(start + 1 , start + k):
                if nums[i] <= nums[i - 1]:
                    return False
            
            return True
        
        
        for i in range(n - 2*k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True
        
        return False
    
sol = Solution()

print(sol.hasIncreasingSubarrays( nums = [2,5,7,8,9,2,3,4,3,1], k = 3))
print(sol.hasIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7], k = 5))                