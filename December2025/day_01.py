from typing import List 

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        THOUGHT:
        --------
        We want to run `n` computers for the maximum equal time T.
        Each battery can contribute at most `min(battery[i], T)` minutes.
        If the total contributed minutes from all batteries is at least `T * n`,
        then running all computers for T minutes is possible.
        
        So the problem reduces to checking if:
            sum(min(battery[i], T)) >= T * n
        
        Since T is monotonic (if we can run for T, we can run for T-1),
        we can apply binary search on T.

        STEPS:
        ------
        1. Compute total battery energy.
        2. Binary search on T from 0 to total // n.
        3. For each mid = T, compute:
                total_contribution = sum(min(b[i], mid))
           If total_contribution >= mid * n → feasible → move right.
           Otherwise → move left.
        4. Return the largest feasible T.

        ALGORITHM:
        ----------
        1. low = 0
        2. high = total // n
        3. While low <= high:
               mid = (low + high) // 2
               if sum(min(b[i], mid)) >= mid * n:
                   ans = mid
                   low = mid + 1
               else:
                   high = mid - 1
        4. Return ans

        TIME COMPLEXITY:
        ----------------
        Sorting not required.
        Binary search runs log(total/n) times.
        Each check is O(m), m = number of batteries.

        Overall: O(m log(total))
        Space:   O(1)
        """
        
        total = sum(batteries)
        
        low , high = 0 , total // n
        ans = 0
        
        while low <= high:
            # current T
            mid = (low + high) // 2
            
            contributed = 0
            for b in batteries:
                contributed += min(b , mid)
            
            if contributed >= mid * n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans 
    
sol = Solution()
print(sol.maxRunTime(n = 2, batteries = [3,3,3]))
print(sol.maxRunTime(n = 2, batteries = [1,1,1,1]))
print(sol.maxRunTime(n = 2 , batteries = [2,2,4,8])) 