from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        
        def simulate(start: int, direction: int) -> bool:
            arr = nums[:]  # make a copy
            curr = start
            dir = direction

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir # move to the same direction
                else:
                    arr[curr] -= 1
                    dir *= -1  # reverse direction
                    curr += dir
            
            # check if all are zero
            return all(x == 0 for x in arr)
        
        count = 0
        for i in range(n):
            if nums[i] == 0:
                # try both directions
                if simulate(i, 1):   # right
                    count += 1
                if simulate(i, -1):  # left
                    count += 1
                    
        return count
        

sol = Solution()
print(sol.countValidSelections([1,0,2,0,3]))