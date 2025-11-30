from typing import List 

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        ## Thoughts:
            The initial idea might be to remove a subarray whose sum equals the
            remainder = total_sum % p. However, this is incorrect because the problem 
            is based on modulo arithmetic, not exact sums. A valid removed subarray 
            only needs to satisfy:  
                removed_sum % p == remainder
                
            This means the removed sum can be larger than 'remainder', since modulo 
            wraps around. Therefore, a simple sliding window does NOT work. Instead,
            we must use prefix sums modulo p and track them in a hash map to efficiently
            detect the smallest subarray whose modulo contribution matches the needed remainder.

        ## Steps:
            1. Compute total_sum and find 'need' = total_sum % p. If need == 0,
               the array is already divisible by p, so return 0.

            2. Use a running prefix sum modulo p. For each index i, compute:
                    prefix = (prefix + nums[i]) % p

            3. To remove the smallest subarray (l..r), we need:
                    (prefix[r] - prefix[l]) % p == need
               This rearranges to:
                    prefix[l] == (prefix[r] - need + p) % p

               So for each prefix[r], compute the target prefix value we need at index l.

            4. Store prefix remainders and their earliest indices in a hashmap.
               Whenever a matching prefix is found, update the answer with the
               shortest possible subarray.

            5. If the resulting length equals the whole array, return -1 (not allowed
               to remove the entire array). Otherwise, return the minimum length.

        ## Algorithm:
            - total = sum(nums)
            - need = total % p
            - If need == 0: return 0

            - Initialize:
                prefix = 0
                seen = {0: -1}   # prefix remainder at index -1
                ans = len(nums)

            - Loop through nums:
                For each index i:
                    prefix = (prefix + nums[i]) % p
                    target = (prefix - need + p) % p
                    If target exists in 'seen', update ans
                    Store prefix in seen with current index

            - If ans == len(nums): return -1
            - Else return ans
            
        # Time Complexity: O(n) cause we are traversing all the element once.
        # Space Complexity: O(n) cause we are using a hashmap to store the prefix. 
        """
        # find the total sum of all elements
        total = sum(nums)
        # Find the remainder which is the needed sub-array sum
        need = total % p 
        if need == 0:
            # already divisible so no need to remove anything
            return 0
        
        prefix = 0
        seen = {0 : -1} # prefix % p at index -1
        ans = len(nums)
        
        for i , num in enumerate(nums):
            prefix = (prefix + num) % p 
            target = (prefix - need) % p 
            
            if target in seen:
                ans = min(ans , i - seen[target])
            
            seen[prefix] = i 
        
        return ans if ans < len(nums) else -1

sol = Solution()

print(sol.minSubarray([3,1,4,2] , 6))
print(sol.minSubarray([6,3,5,2] , 9))
print(sol.minSubarray([1,2,3,2,3] , 3)) 