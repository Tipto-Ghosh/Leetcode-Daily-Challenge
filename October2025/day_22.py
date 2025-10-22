from typing import List
from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Frequency of exact values
        freq = Counter(nums)

        # Build interval endpoints
        lefts = [x - k for x in nums]
        rights = [x + k for x in nums]

        # Sort endpoints for binary searches
        lefts.sort()
        rights.sort()

        # 1) Compute maximum overlap (cover) of intervals at any point using sweep-line.
        # We'll create events (pos, delta). We use right + 0.5 as the "just after" the inclusive right end,
        # so integer coordinates are handled correctly without off-by-one complexities.
        events = []
        for a, b in zip(lefts, rights):
            events.append((a, 1))
            events.append((b + 0.5, -1))  # subtract after the inclusive right endpoint

        events.sort()
        cover = 0
        max_cover_any_point = 0
        for pos, delta in events:
            cover += delta
            if cover > max_cover_any_point:
                max_cover_any_point = cover

        # Candidate from a T that is not equal to any existing nums-value:
        # best_non_existing_T = min(max_cover_any_point, numOperations)
        best = min(max_cover_any_point, numOperations)

        # 2) Evaluate every distinct T present in nums
        # For a given T, number of intervals covering T:
        #   cover(T) = number of lefts <= T  minus number of rights < T
        # where bisect_right(lefts, T) gives count of lefts <= T,
        # and bisect_left(rights, T) gives count of rights < T.
        for T, cnt_equal in freq.items():
            cover_T = bisect_right(lefts, T) - bisect_left(rights, T)
            candidate = min(cover_T, cnt_equal + numOperations)
            if candidate > best:
                best = candidate

        return best

# quick checks
sol = Solution()
print(sol.maxFrequency([1,4,5], 1, 2))   # expected 2
print(sol.maxFrequency([5,64], 42, 2))   # expected 2
print(sol.maxFrequency([5,11,20,20], 5, 1)) # expected 2
