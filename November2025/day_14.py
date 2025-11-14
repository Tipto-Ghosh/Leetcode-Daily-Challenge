from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        # 2D difference array of size (n+1) x (n+1)
        # We use n+1 to handle boundary updates safely
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Apply each query to the difference matrix
        for row1, col1, row2, col2 in queries:

            # Mark the +1 at the top-left of the submatrix
            diff[row1][col1] += 1

            # Mark -1 just below the bottom boundary
            diff[row2 + 1][col1] -= 1

            # Mark -1 just right of the right boundary
            diff[row1][col2 + 1] -= 1

            # Cancel out the extra subtraction at bottom-right corner
            diff[row2 + 1][col2 + 1] += 1

        # Now build the final matrix using 2D prefix sum
        mat = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):

                # prefix from top
                top = mat[i - 1][j] if i > 0 else 0

                # prefix from left
                left = mat[i][j - 1] if j > 0 else 0

                # prefix from top-left (to remove double counting)
                top_left = mat[i - 1][j - 1] if i > 0 and j > 0 else 0

                # Standard 2D prefix sum formula:
                # prefix[i][j] = diff[i][j] + top + left - top_left
                mat[i][j] = diff[i][j] + top + left - top_left

        return mat

sol = Solution()
print(sol.rangeAddQueries(n = 2, queries = [[0,0,1,1]]))