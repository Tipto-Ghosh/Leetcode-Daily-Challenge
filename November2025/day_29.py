from typing import List 

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """ 
        # Observations:
          operation: replace nums[i] with nums[i] - 1
        
        # Thoughts:
        If total sum of all the elements needed to be divisible by k then
        Every element should divisible by k or sum of all the remainder divisible by k.
        
        What we can do is go to each element and find the remainder and sum all these
        remainder and then divide the remainder by k and find the remainder again this
        will be the minimum operation count, cause this last remainder is the extra value that
        we need to remove and at one operation we can decrease only one.
        
        # Algorithm:
          rem = 0
          1. traverse all the element
          2. find the remainder
          3. sum up all the remainder
          4. find the remainder of the remainder
          5. return the last calculated remainder
        
        # Time Complexity: O(n) cause we are traversing all the element once.
        # Space Complexity: O(1) cause we are not using any extra space.
        """
        
        # track the remainder
        rem = 0
        
        # traverse all the elements
        for num in nums:
            # find the remainder and add with rem
            rem += num % k 
        
        # find the remainder of the remainders
        rem %= k 
        return rem

sol = Solution()

print(sol.minOperations([3,9,7] , 5))
print(sol.minOperations([3,4,1] , 4))
print(sol.minOperations([3,2] , 6))