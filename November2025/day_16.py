class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        ans = 0
        count_ones = 0
        
        for i in range(n):
            # count the number of continous ones 
            if s[i] == '1':
                count_ones += 1
            else:
                # find the count sub-string
                sub_str = (count_ones * (count_ones + 1)) // 2
                ans = (ans + sub_str) % MOD
                count_ones = 0      
        
        # count the last sub-string
        sub_str = (count_ones * (count_ones + 1)) // 2
        ans = (ans + sub_str) % MOD
        return ans 
    

sol = Solution()

print(sol.numSub('0110111'))
print(sol.numSub('101'))