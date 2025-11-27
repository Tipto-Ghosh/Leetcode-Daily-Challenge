from typing import List 

class Solution:
    def maxSubarraySum(self, arr: List[int], k: int) -> int:
        """
        ## Thought process:
        we want a subarray from index i to j where:
        (j - i) % k = 0 and it's sum is maximum.
        
        now:
        => (j - i) % k = 0
        => j % k - i %k = 0
        => j % k = i % k -----> eqn(1)
        
        let's build a prefix sum array where
        prefix[x] = arr[0] + arr[1] + ....... + arr[x-1]
        
        Now if we want to find the sum of all elements of a subarray index i to j
        subarray_sum = prefix[j] - prefix[i]
        
        now as we want the subarray length must need to be divided by k so we have to maintain the eqn(1)
        So at any index j we have to find out the remainder r = j % k
        now all index i is valid if i % k = r from i = 0 to j-1
        so for index i = 0.....j-1 we have to find the subarray_sum and take the max one.
        
        Now think for a moment, do we need to check all the previous(i) subarray sum!!
        No we want to maximize the subarray sum so sum will be maximize if we substract a minimum number from prefix[j]
        means we want the smallest prefix[i] where i % k = j % k
        
        # Algorithm:
        step-01: Find the prefix sum
        step-02: Find the rem = j % k 
        step-03: Find the subarray_sum = prefix[j] - min value for the remainder rem
        step-04: Update the min value for remainder if we got more smaller value than previous
        step-05: Store the max sub_array_sum as answer
        
        => repeat all these steps from index 0 to n - 1 where n is the length of array.     
        
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        
        # prefix holds sum of nums[0.......j] after adding j
        prefix = 0
        INF = float('INF')
        
        # best[r] = smallest prefix sum seen so far for indices with index % k == r
        best = [INF] * k # length k cause maximum remainder can be 0 to k-1
        
        # consider the prefix before the array starts(sum = 0) as index -1 with remainder 0
        best[0] = 0
        
        n = len(arr)
        ans = -INF
        
        for j in range(n):
            # make the prefix sum
            prefix += arr[j]
            # Find the remainder using the prefix index and index j corresponds to prefix index j + 1
            r = (j + 1) % k 
            # find the subarray_sum = prefix - best[r]
            subarray_sum = prefix - best[r]
            # store the max sum as ans
            if subarray_sum > ans:
                ans = subarray_sum
            
            # update best[r] if we got smaller sum for remainder r
            if prefix < best[r]:
                best[r] = prefix
        
        return ans 
    
sol = Solution()

print(sol.maxSubarraySum([1,2] , 1))
print(sol.maxSubarraySum([-1,-2,-3,-4,-5] , 4))
print(sol.maxSubarraySum([-5,1,2,-3,4] , 2))