from typing import List 

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7 
        n = len(complexity)
        
        root = complexity[0] # root unlocked computer
        
        # if there is any computer with complexity less than equal to root
        # it can never be unlocked so ans will be 0 cause no valid permuations
        for i in range(1 , n):
            if complexity[i] <= root:
                return 0
        
        
        # if all the computers are unlockable and
        # there is no dependency among them now.
        # number of permutation will be (n - 1) % MOD
        
        # calculating factorial of (n-1)! 
        fact = 1  
        for i in range(1 , n):
            fact = (fact * i) % MOD 
        
        return fact 
    
sol = Solution()
print(sol.countPermutations([1,2,3]))
print(sol.countPermutations([3,3,3,4,4,4]))