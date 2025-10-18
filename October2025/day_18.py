from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        count_dis = 0
        prev = - float('INF')
        
        for num in nums:
            curr = min(max(prev + 1 , num - k) , num + k)
            if curr > prev:
                count_dis += 1
                prev = curr
        
        return count_dis