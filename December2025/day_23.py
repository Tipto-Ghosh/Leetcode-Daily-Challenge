from typing import List
from collections import defaultdict
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # sort based on the start value
        events = sorted(events , key = lambda x:x[0])
        n = len(events)
        max_suffix = [0] * n
        
        max_suffix[-1] = events[-1][2]
        for i in range(n-2 , -1 , -1):
            max_suffix[i] = max(max_suffix[i + 1] , events[i][2])
        
        ans = 0
        
        for i , (start , end , value) in enumerate(events):
            # using BS find the event which starting is greater than curr_end
            left , right = i + 1 , n - 1
            # find the smallest starting point greater than curr_end
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > end: # non-overlap
                    right = mid - 1
                else:
                    left = mid + 1
            if left < n:
                ans = max(ans , value + max_suffix[left])
            ans = max(ans , value)
        return ans