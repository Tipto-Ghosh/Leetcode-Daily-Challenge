from typing import List 
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev_one_pos = -1 # position of previous one
        
        for i in range(n):
            if nums[i] == 1:
                # if prev_one_pos is -1 means this i-th index is the first one, which is okay
                # if distance between current and previous one is >= k, then it's also okay
                if not (prev_one_pos == -1 or i - prev_one_pos - 1 >= k):
                    return False
                # update the one's position
                prev_one_pos = i  
        
        return True 


sol = Solution()
print(sol.kLengthApart([1,0,0,0,1,0,0,1], k = 2))
print(sol.kLengthApart([1,0,0,1,0,1], k = 2))