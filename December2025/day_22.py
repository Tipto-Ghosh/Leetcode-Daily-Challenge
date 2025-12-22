class Solution:
    def minDeletionSize(self, A):
        # Number of columns in each string
        W = len(A[0])

        # dp[i] stores the length of the longest non-decreasing
        # column sequence starting from column i
        dp = [1] * W   # Every column alone is a valid sequence

        # Traverse columns from right to left
        # because dp[i] depends on dp[j] where j > i
        for i in range(W - 2, -1, -1):
            # Check all columns to the right of i
            for j in range(i + 1, W):
                # Check if column i can come before column j
                # i.e., for every row, A[row][i] <= A[row][j]
                if all(row[i] <= row[j] for row in A):
                    # If valid, update dp[i] by extending dp[j]
                    dp[i] = max(dp[i], 1 + dp[j])

        # We want to keep the longest valid column sequence
        # Minimum deletions = total columns - longest sequence
        return W - max(dp)
