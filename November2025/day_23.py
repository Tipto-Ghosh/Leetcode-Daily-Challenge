from typing import List 

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Divide numbers into three groups based on remainder when divided by 3
        # a -> numbers divisible by 3
        # b -> numbers giving remainder 1
        # c -> numbers giving remainder 2
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        # Initial answer
        ans = 0

        # Lengths of groups b and c
        lb, lc = len(b), len(c)

        # Try removing the minimal number of elements from b and c
        # to make the sum divisible by 3.
        # Because any valid combination must satisfy:
        # (count of selected from b - count of selected from c) % 3 == 0
        #
        # We test combinations where we remove 0, 1, or 2 elements from the end
        # (since removing smallest elements reduces loss)
        for cntb in [lb - 2, lb - 1, lb]:
            # cntb = how many largest elements from b we keep
            if cntb >= 0:
                for cntc in [lc - 2, lc - 1, lc]:
                    # cntc = how many largest elements from c we keep
                    if cntc >= 0 and (cntb - cntc) % 3 == 0:
                        # Update answer with max sum obtained from selected elements
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        
        # Add the always-valid contribution from 'a'
        return ans + sum(a)

sol = Solution()
print(sol.maxSumDivThree([3,6,5,1,8]))