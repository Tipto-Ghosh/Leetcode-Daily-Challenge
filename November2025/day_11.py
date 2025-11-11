from typing import List 

class Solution:
    # Solve Using Memoization
    def solveMemo(self, index, m, n, size, arr, dp):
        # Base Case
        if index >= size:
            return 0
        if m < 0 or n < 0:
            return 0

        if dp[index][m][n] != -1:
            return dp[index][m][n]

        # Count 0s and 1s in current string
        count0 = arr[index].count('0')
        count1 = arr[index].count('1')

        include = 0
        # Include current string if possible
        if m >= count0 and n >= count1:
            include = 1 + self.solveMemo(index + 1, m - count0, n - count1, size, arr, dp)

        # Exclude current string
        exclude = self.solveMemo(index + 1, m, n, size, arr, dp)

        dp[index][m][n] = max(include, exclude)
        return dp[index][m][n]

    def findMaxForm(self, arr, m, n):
        size = len(arr)
        dp = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(size)]
        return self.solveMemo(0, m, n, size, arr, dp)
