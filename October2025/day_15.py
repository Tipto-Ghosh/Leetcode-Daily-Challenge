from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        """ 
        We need two adjacent strictly increasing subarrays of the same length k. That means:
        nums[i .. i + k - 1] -> strictly increasing
        nums[i + k .. i + 2k - 1] -> strictly increasing
        This 2 parts exists in the same nums array.
        
        Steps to Solve:
        1. Compute the length of increasing sub-array starting at index i
        2. Compute the length of increasing sub-array ending at index i
        3. Then for each i check:
           -> if both increasing segment ending at i and starting at i + 1 are same then it's the value of k.
        Our goal is to find the max k
        """ 
        
        n = len(nums)
        increasingStarts = [1 for _ in range(n)]
        increasingEnds = [1 for _ in range(n)]
        
        # increasing lengths ending at i
        for i in range(1 , n):
            if nums[i - 1] < nums[i]:
                increasingEnds[i] = increasingEnds[i - 1] + 1
        
        # increasing lengths starts at i
        for i in range(n - 2 , -1 , -1):
            if nums[i + 1] > nums[i]:
                increasingStarts[i] = increasingStarts[i + 1] + 1
                
        # now check adjacent boundary for each i
        k = 0
        for i in range(n - 1):
            temp_k = min(increasingEnds[i] , increasingStarts[i + 1])
            k = max(k , temp_k)
        
        return k 
    
sol = Solution()

print(sol.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))
print(sol.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))  