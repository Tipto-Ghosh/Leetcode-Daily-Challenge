class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        # store the positions of the seats
        seats = [i for i,ch in enumerate(corridor) if ch == 'S']
        
        # if no seats or odd number of seats we cant divide
        if len(seats) == 0 or len(seats) % 2 == 1:
            return 0
        
        ways = 1
        # Look at gaps between every pair of seat-pairs
        for i in range(2 , len(seats) , 2):
            plants_between = seats[i] - seats[i - 1] - 1
            ways = (ways * (plants_between + 1)) % MOD 
        
        return ways 
    
sol = Solution()

print(sol.numberOfWays("SSPPSPS")) # 3
print(sol.numberOfWays("PPSPSP")) # 1
print(sol.numberOfWays("S")) # 0