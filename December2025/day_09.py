from typing import List

class Solution: 
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # num_cnt[v] = how many times value v appears in the whole array.
        # This helps us know how many occurrences remain to the RIGHT of current index.
        num_cnt = {}
        
        # num_partial_cnt[v] = how many times value v has appeared so far
        # while scanning from left to right.
        # This helps us count occurrences on the LEFT of current index.
        num_partial_cnt = {}

        # Pre-calc total counts of each number (for right-side counting later)
        for v in nums:
            num_cnt[v] = num_cnt.get(v, 0) + 1

        ans = 0
        
        # Iterate j from left to right:
        # For each nums[j], we count valid i < j and valid k > j.
        for v in nums:
            # This v is nums[j]
            target = v * 2

            # Count how many values equal to nums[j] * 2 appear BEFORE index j.
            # i.e., nums[i] == 2 * nums[j]
            l_cnt = num_partial_cnt.get(target, 0)

            # Now include nums[j] into "left side count" for future j positions.
            num_partial_cnt[v] = num_partial_cnt.get(v, 0) + 1

            # Count how many values equal to nums[j] * 2 appear AFTER index j.
            # These are total occurrences minus the ones already passed.
            r_cnt = num_cnt.get(target, 0) - num_partial_cnt.get(target, 0)

            # Contribution of this index j:
            # Any left match (i) can pair with any right match (k)
            # forming l_cnt * r_cnt special triplets.
            ans = (ans + l_cnt * r_cnt) % MOD

        return ans

    
sol = Solution()

print(sol.specialTriplets([6,3,6]))
print(sol.specialTriplets([0,1,0,0]))
print(sol.specialTriplets([8,4,2,8,4]))

print(sol.specialTriplets([16,8,4,2,4,2,8,4]))