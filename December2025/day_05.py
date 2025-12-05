from typing import List 

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        ### What the problem actually wants?
            Count the maximum number of sub-array where 
            the difference between the sum of the left and right subarrays is even.
            
        ### Key Observations
           -> even - even = even
           -> odd - odd = even
           If current sub-array sum is even then left and right sub-array
           sum also need to be even and vice-versa.
           
           So For a single element we need to check its left portions sum and right portions sum.
           If they have same parity. if yes then we have a valid sub-array. So we need to maintain
           a left sum and right sum.
        
        ### Steps of the Algorithm
            - Find the sum of all elements which will be the right side sum.
            - now lets say no partition so left_sum is 0 and right sum total of nums.
            - now start partitioning at every index i
            - If we partition at i then value of index i will be the part of left sum
            - value of index i need to remove from right sum
            - if left sum and right sum difference is even then it's a valid partition.
        
        ### Time Complexity:  O(n)
        ### Space Complexity: O(1)
        """
        
        # right sum is the total cause till now no partion all the element are in the right side
        right_sum = sum(nums)
        # As no partition took place so left sub-array has no element so sum is 0
        left_sum = 0
        # count the number of possible sub-array
        count = 0
        
        # start doing partition from index 0 to n-2 index
        # Why not last index is included cause if we include last index also then one sub-array will be empty
        for i in range(len(nums) - 1):
            # partition at index i
            # so from index 0 to i is in left-subarray
            left_sum += nums[i]
            # as value of index i is a part of left-subarray so remove it from right-subarray
            right_sum -= nums[i] 
            # check if both left and right partition sum difference is even or not
            if abs(right_sum - left_sum) % 2 == 0:
                count += 1 # if even then increment the count
        
        return count
        
sol = Solution()

print(sol.countPartitions([10,10,3,7,6]))
print(sol.countPartitions([1,2,2]))
print(sol.countPartitions([2,4,6,8]))