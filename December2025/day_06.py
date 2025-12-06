from typing import List 
from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """  
        ### What the problem actually wants?

            We have an array nums of length n.
            We want to split it into one or more CONTIGUOUS segments.

            Each segment must satisfy:
                max(segment) - min(segment) ≤ k

            A "partition" = cutting the array into valid segments.

        Our task:
            Count how many different valid partitions exist.
            Return answer modulo (1e9 + 7).

        ### Key Observations

            Suppose we fix the right boundary of a segment at index i.
            We want to find all starting positions j such that:
                    nums[j..i] is valid
                    -> meaning max(nums[j..i]) - min(nums[j..i]) ≤ k

            Important insight:
                If nums[j..i] is valid,
                then nums[j+1..i], nums[j+2..i], ... are ALSO valid.
            
            That means:
                Valid starting points j form a CONTINUOUS interval [L, i].

            So:
                dp[i+1] = dp[L] + dp[L+1] + ... + dp[i]

            Where:
                dp[x] = number of valid partitions for prefix nums[0..x-1]
            
            And:
                dp[0] = 1 (empty array has exactly 1 way)

            But summing dp[L..i] every time is too slow ⇒ O(n²).

        ### Optimizing with Prefix Sums

            Define prefix sums:
                prefix[x] = dp[0] + dp[1] + ... + dp[x-1]

            Then:
                dp[i+1] = prefix[i] - prefix[L-1]

            Just need to find L efficiently for every i.

        ### The Real Problem: How to find L?

            We use a sliding window [L..i]:

                - Expand i to the right
                - Maintain current max and min in the window
                - If (max - min > k), shrink L

            Tools:
                Use two monotonic deques:
                    - One for max values
                    - One for min values

            These allow:
                O(1) updates per element
                -> entire window logic is O(n)

            After adjusting L, the window nums[L..i] becomes valid.

            Then dp[i+1] can be computed instantly using prefix sums.

        ### Variables:

            dp[i]  = number of partitions for prefix ending at i-1
            prefix = running prefix sums of dp
            L      = left boundary of valid window
            maxQ   = monotonic decreasing queue (max)
            minQ   = monotonic increasing queue (min)

        ### Steps of the Algorithm

            1) Initialize:
                dp[0] = 1
                prefix[0] = 1
                L = 0
                maxQ = minQ = empty

            2) For each i from 0 to n-1:
                    Insert nums[i] into maxQ and minQ correctly.

                    While (maxQ[0] - minQ[0] > k):
                        Remove nums[L] from queues if needed
                        L += 1

                    Now window nums[L..i] is valid.

                    dp[i+1] = prefix[i] - prefix[L-1]
                    prefix[i+1] = prefix[i] + dp[i+1]

            3) Answer = dp[n]

        ### Time Complexity:  O(n)
        ### Space Complexity: O(n)
        """
        MOD = 10**9 + 7
        n = len(nums)

        # dp[i] = number of ways for prefix nums[0..i-1]
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[0] = 1 
        prefix[0] = 1

        L = 0  # left boundary of window
        maxQ = deque()  # decreasing queue for max
        minQ = deque()  # increasing queue for min

        for i in range(0, n):

            # ---- Insert nums[i] into maxQ ----
            while maxQ and maxQ[-1] < nums[i]:
                maxQ.pop()
            maxQ.append(nums[i])

            # ---- Insert nums[i] into minQ ----
            while minQ and minQ[-1] > nums[i]:
                minQ.pop()
            minQ.append(nums[i])

            # ---- Shrink window until valid ----
            while maxQ[0] - minQ[0] > k:
                # Remove nums[L] if they exit the window
                if maxQ[0] == nums[L]:
                    maxQ.popleft()
                if minQ[0] == nums[L]:
                    minQ.popleft()
                L += 1

            # Window [L..i] is now valid
            # Valid starting points = L..i
            # dp[i+1] = prefix[i] - prefix[L-1]
            left_prefix = prefix[L - 1] if L > 0 else 0

            dp[i + 1] = (prefix[i] - left_prefix) % MOD

            # Update prefix
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % MOD

        return dp[n]
    
sol = Solution()
print(sol.countPartitions(nums = [9,4,1,3,7], k = 4))
print(sol.countPartitions(nums = [3,3,4], k = 0))