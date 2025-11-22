from typing import List 
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """ 
        Go to each element and do following:
           Find the remainder by doing this: element % 3
           number of operation needed to make it divisible 3 is:
           remainder can be 0,1,2. If it 0 then it's already divisible by 3. Do nothing
           
           If remainder is 1 or 2 then we can choose 2 things:
            doing add operation 2 times
            doing substract operation 1 time to make it equal to 3 or 0
            Choose the minimum
        
        Time complexity: O(n) cause we are traversing the array once.
        Space complexity: O(1) cause we are not using any extra memory.
        """
        ans = 0 # count of operations
        
        # go to each element of the list
        for element in nums:
            # find the remainder of 3
            rem = element % 3
            
            # if remainder is 2 or 1 then we have to do 1 operation
            # we can add or substract 1 time otherwise no need any operation
            # No matter which one we do we just need to track the operation count
            if rem > 0: # rem == 1 or rem == 2
                ans += 1
                
        return ans 

sol = Solution()

print(sol.minimumOperations([1,2,3,4]))
print(sol.minimumOperations([3,6,9]))