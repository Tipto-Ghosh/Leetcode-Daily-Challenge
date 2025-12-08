class Solution:
    def countTriples(self, n: int) -> int:
        """
        we need to find the triple(a,b,c) where a^2 + b^2 = c^2
        
        if we take a and b as 2 individual number and find the square sum
        of them res = a^2 + b^2 and square root it c = sqrt(res) and 
        c <= n then we got a valid triple (a,b,c)
        
        for a from 1 to n-3(inclusive):
           for b from a+1 to n-2(inclusive):
               if sqrt(a^2 + b^2) <= n:
                  count += 1
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        Optimization: 
          Fix the c so now for every c try all a where a < c
          b^2 = c^2 - a^2
          We can precompute the squres so that we can quickly check for b^2.
          
          Outer loop runs n times 
          inner loop runs c times -> roughly n/2 times on avg.
          Time Complexity: O((n^2) / 2)
          Space Complexity: O(n) cause storing the squares
          
        """
        count = 0
        
        # iterate over all the values of a from 1 to n
        for a in range(1 , n + 1):
            # iterate over all the values of b from 1 to n
            for b in range(1 , n + 1):
                # calculate c^2
                c_square = a**2 + b**2
                # Find c  = sqrt(c_square)
                c = c_square ** 0.5
                
                # now check 2 things
                # 1. c is a integer number
                # 2. c is in this range 1<= c <= n
                if c % 1 == 0 and 1 <= c <= n:
                    count += 1
        
        return count 
    
    
sol = Solution()
print(sol.countTriples(5))
print(sol.countTriples(10))