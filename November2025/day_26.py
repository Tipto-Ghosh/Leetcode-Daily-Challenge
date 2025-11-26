from typing import List 
from functools import lru_cache

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        Rows , Cols = len(grid) , len(grid[0])

        """
        @lru_cache(None)
        def traverse(row: int , col: int , rem: int) -> int:
            # if we are out of bounds
            if row < 0 or row >= Rows or col < 0 or col >= Cols:
                return 0 # no path
            
            # if we are at goal state
            if row == Rows - 1 and col == Cols - 1:
                # check if divisible by k or not
                return 1 if (rem + grid[row][col]) % k == 0 else 0
            
            count = 0 # possible path count from this state
            
            new_rem = (rem + grid[row][col]) % k
            
            # we have 2 options to move down and right
            
            # move to the right
            right = traverse(row , col + 1 , new_rem) 
            count = (count + right) % mod 
            
            # move to the down
            down = traverse(row  + 1 , col , new_rem) 
            count = (count + down) % mod
                         
            return count
        
        return traverse(0 , 0 , 0)           
        """
        
        # converting to Bottom-up
        m , n = len(grid) , len(grid[0])
        # -------------------------------------------------------------
        # dp[i][j][r] = number of ways to reach cell (i-1, j-1) such that the path sum % k == r
        # We use (m+1) x (n+1) indexing so that dp[1][1] corresponds to grid[0][0]
        # This avoids boundary checks for dp[i-1][j] and dp[i][j-1].
        # -------------------------------------------------------------
        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]

        # -------------------------------------------------------------
        # Base Case:
        # The first cell (1,1) corresponds to grid[0][0].
        # Only one path exists: stay on this cell.
        # The remainder is grid[0][0] % k.
        # -------------------------------------------------------------
        dp[1][1][grid[0][0] % k] = 1

        # -------------------------------------------------------------
        # Fill DP table row by row (bottom-up).
        #
        # For each cell (i, j):
        #   - value = grid[i-1][j-1] % k   # current cell’s value modulo k
        #   - We want to compute dp[i][j][r] for all r in [0…k-1]
        #
        # For each remainder r:
        #   We need to know how many ways we could come from top or left
        #   with some previous remainder 'prev_mod' such that:
        #
        #   (prev_mod + value) % k == r
        #
        #   => prev_mod = (r - value + k) % k
        #
        #   Then:
        #     dp[i][j][r] =
        #         dp[i-1][j][prev_mod]   # from top
        #       + dp[i][j-1][prev_mod]   # from left
        # -------------------------------------------------------------
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Skip (1,1) since it's already initialized
                if i == 1 and j == 1:
                    continue

                # current cell's value modulo k
                value = grid[i - 1][j - 1] % k

                # Calculate #ways for each remainder r
                for r in range(k):
                    # Find the needed remainder BEFORE entering this cell
                    prev_mod = (r - value + k) % k

                    # number of ways = ways from top + ways from left
                    dp[i][j][r] = (
                        dp[i - 1][j][prev_mod] + dp[i][j - 1][prev_mod]
                    ) % mod

        # -------------------------------------------------------------
        # Answer:
        # dp[m][n][0] = number of ways to reach bottom-right cell
        #               such that total path sum % k == 0
        # -------------------------------------------------------------
        return dp[m][n][0]
        
        
sol = Solution()
print(sol.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3))
print(sol.numberOfPaths(grid = [[0,0]], k = 5))
print(sol.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1))            