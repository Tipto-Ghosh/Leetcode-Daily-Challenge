from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        operations = 0
        
        for ele in nums:
            while stack and stack[-1] > ele:
                stack.pop()
            
            if ele == 0:
                continue
            
            if not stack or stack[-1] < ele:
                operations += 1
                stack.append(ele)
        
        return operations

sol = Solution()

print(sol.minOperations([3,1,2,1]))