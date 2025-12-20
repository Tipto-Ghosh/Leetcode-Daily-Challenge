from typing import List 

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        cols = len(strs[0])
        
        delete_cols = 0
        
        # go to each column
        for col in range(cols):
            # go to each letter of this column for all strs
            letters = []
            for i in range(1 , n):
                # letters.append((strs[i - 1][col] , strs[i][col]))
                # check same column of prev str should be less than equal to the current str col
                if strs[i - 1][col] > strs[i][col]: 
                    # so we need to delete this col
                    delete_cols += 1
                    break
            # print(letters)
        return delete_cols
    
sol = Solution()

print(sol.minDeletionSize(["abc", "bce", "cae"]))
print(sol.minDeletionSize(["cba","daf","ghi"]))
print(sol.minDeletionSize(["a","b"]))
print(sol.minDeletionSize(["zyx","wvu","tsr"]))