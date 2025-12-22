from typing import List 


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        def is_sorted(arr: List[str]) -> bool:
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        ans = 0
        
        # cur keeps the constructed strings row-wise
        cur = [""] * len(A)

        for col in zip(*A):
            # Try adding this column to cur
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] += letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans


        
sol = Solution()

print(sol.minDeletionSize(["xc","yb","za"]))