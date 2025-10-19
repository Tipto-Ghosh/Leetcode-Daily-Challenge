from typing import List
from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Key Observations:
        
        1. Rotation repeats after len(s) steps.
            Because after len(s) rotations, we get the same string back.
        2. Adding a to odd indices cycles after at most 10 steps.
            Because digits wrap around modulo 10, and applying the operation 10 times will bring digits back to original.

        So , there are at most len(s) * 10 distinct states possible.
        This means we can use BFS or DFS to explore all reachable strings and track the lexicographically smallest.
        """
        
        def add_a(curr):
            """Add a to all the odd indices"""
            num = []
            for i in range(len(curr)):
                val = int(curr[i])
                if i % 2 == 1:
                    val = (val + a) % 10
                num.append(str(val))
            
            return ''.join(num)
        
        def rotate_b(curr):
            right = curr[-b : ]
            left = curr[ : -b]
            return right + left 
                     
        
        seen = set() # store all the seen numbers
        queue = deque([s])
        smallest = s 
        
        while queue:
            curr = queue.popleft()
            # if curr is seen before then skip
            if curr in seen:
                continue
            
            # add curr to seen
            seen.add(curr)
            # take the min number
            if curr < smallest:
                smallest = curr 
            
            # apply operation-1: Add a to all odd indices
            added = add_a(curr)
            # apply operation-2: rotate right by b
            rotated = rotate_b(curr)
            
            # add this 2 new number in to queue
            queue.append(added)
            queue.append(rotated)
        
        return smallest
            
            
            
# arr = [3,4,5,6]
# right = arr[-1 : ]
# left = arr[ : -1]
# print(right)
# print(left)
# print(right + left)

sol = Solution()
print(sol.findLexSmallestString(s = "5525", a = 9, b = 2))
print(sol.findLexSmallestString(s = "74", a = 5, b = 1))
print(sol.findLexSmallestString(s = "0011", a = 4, b = 2))